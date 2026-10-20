"""Create chapter-one slides, Mandarin speech, captions and a browser-playable MP4.

Requires ffmpeg/ffprobe and the Python packages in requirements.txt.
Usage: python3 scripts/course-video/generate.py --font /path/to/chinese-font.ttc
Speech synthesis sends only the public lesson narration to the Edge TTS service.
"""
import argparse
import asyncio
import hashlib
import json
import re
import subprocess
from pathlib import Path

import edge_tts
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name('chapter01.json')
OUTPUT = ROOT / 'src/.vuepress/public/videos/chapter01'


def command(args):
    return subprocess.check_output(args, text=True, stderr=subprocess.STDOUT)


def duration(path):
    return float(command(['ffprobe', '-v', 'error', '-show_entries',
                          'format=duration', '-of', 'default=nw=1:nk=1', str(path)]))


def wrap(text, font, width, draw):
    lines, line = [], ''
    for char in text:
        if draw.textlength(line + char, font=font) > width and line:
            lines.append(line)
            line = char
        else:
            line += char
    if line:
        lines.append(line)
    return lines


def slide_image(slide, index, total, font_path, target):
    image = Image.new('RGB', (1280, 720), '#0c1528')
    draw = ImageDraw.Draw(image)
    font = lambda size: ImageFont.truetype(font_path, size)
    small, body, heading, key_font = font(20), font(29), font(43), font(25)
    draw.rectangle((0, 0, 1280, 7), fill='#45d6b0')
    draw.text((62, 37), '计算机系统原理  /  13015', font=small, fill='#9aabc4')
    label_width = draw.textlength(slide['label'], font=small)
    draw.text((1218-label_width, 37), slide['label'], font=small, fill='#45d6b0')
    for y, line in enumerate(wrap(slide['title'], heading, 1160, draw)):
        draw.text((60, 98+y*56), line, font=heading, fill='#f7fafc')
    draw.line((62, 181, 1218, 181), fill='#293a53', width=2)
    y = 211
    for point in slide['points']:
        draw.ellipse((65, y+13, 73, y+21), fill='#45d6b0')
        lines = wrap(point, body, 1095, draw)
        for line in lines:
            draw.text((94, y), line, font=body, fill='#e0e8f2')
            y += 43
        y += 15
    draw.rounded_rectangle((60, 506, 1220, 582), radius=14, fill='#193344')
    for i,line in enumerate(wrap(slide['key'], key_font, 1090, draw)):
        draw.text((84, 527+i*31), line, font=key_font, fill='#7cedd0')
    draw.text((62, 680), '第一章复习讲解 · 普通话配音', font=small, fill='#8295b2')
    draw.text((1120, 680), f'{index+1:02d} / {total:02d}', font=small, fill='#8295b2')
    image.save(target)


def timestamp(seconds, vtt=False):
    ms = round(seconds * 1000)
    h, rem = divmod(ms, 3600000)
    m, rem = divmod(rem, 60000)
    s, ms = divmod(rem, 1000)
    return f'{h:02d}:{m:02d}:{s:02d}{"." if vtt else ","}{ms:03d}'


def speech_complete(slide, events):
    normalize = lambda text: re.sub(r"[\W_]+", "", text).lower()
    expected = normalize(slide['narration'])
    spoken = normalize(''.join(e.get('text', '') for e in events))
    return len(spoken) >= len(expected) * 0.95 and spoken.endswith(expected[-15:])


def speech_captions(events):
    # Keep groups short enough to fit a single, readable subtitle line.
    cues, text, start, end = [], '', 0, 0
    for event in events:
        if event.get('type') != 'WordBoundary':
            continue
        word = event['text']
        if text and len(text + word) > 34:
            cues.append((start, end, text))
            text = ''
        if not text:
            start = event['offset'] / 1e7
        text += word
        end = (event['offset'] + event['duration']) / 1e7
    if text:
        cues.append((start, end, text))
    if not cues:
        raise RuntimeError('The speech service returned no subtitle timestamps')
    return cues


async def make_speech(slide, index, cache, voice, rate, semaphore):
    base = cache / f'{index:02d}'
    audio, metadata = base.with_suffix('.mp3'), base.with_suffix('.json')
    identity = hashlib.sha256((slide['narration'] + voice + rate).encode()).hexdigest()
    if audio.exists() and metadata.exists():
        saved = json.loads(metadata.read_text())
        if saved['identity'] == identity and audio.stat().st_size > 100 and speech_complete(slide, saved['events']):
            return audio, speech_captions(saved['events'])
    async with semaphore:
        for attempt in range(3):
            try:
                stream = edge_tts.Communicate(slide['narration'], voice,
                                              rate=rate, boundary='WordBoundary',
                                              connect_timeout=20, receive_timeout=45)
                events = []
                with audio.open('wb') as f:
                    async for event in stream.stream():
                        if event['type'] == 'audio':
                            f.write(event['data'])
                        else:
                            events.append(event)
                if not speech_complete(slide, events):
                    raise RuntimeError(f'Incomplete narration in section {index+1}')
                cues = speech_captions(events)
                metadata.write_text(json.dumps({'identity': identity, 'events': events},
                                               ensure_ascii=False))
                print(f'Speech {index+1}: {duration(audio):.1f}s', flush=True)
                return audio, cues
            except Exception:
                if attempt == 2:
                    raise
                await asyncio.sleep(2)


async def main(args):
    slides = json.loads(SOURCE.read_text())
    OUTPUT.mkdir(parents=True, exist_ok=True)
    cache = Path(args.cache).resolve()
    cache.mkdir(parents=True, exist_ok=True)
    semaphore = asyncio.Semaphore(2)
    speech = await asyncio.gather(*(make_speech(s, i, cache, args.voice, args.rate, semaphore)
                                    for i,s in enumerate(slides)))
    all_cues, chapters, segments, elapsed = [], [], [], 0.0
    for i,(slide,(audio,cues)) in enumerate(zip(slides,speech)):
        image, subtitles, video = (cache / f'{i:02d}{ext}' for ext in ('.png','.srt','.mp4'))
        slide_image(slide, i, len(slides), args.font, image)
        subtitles.write_text('\n\n'.join(f'{j+1}\n{timestamp(a)} --> {timestamp(b)}\n{t}'
                                         for j,(a,b,t) in enumerate(cues))+'\n')
        # A short final pause makes section changes easier to follow.
        seconds = duration(audio) + 0.65
        style = 'FontName=Microsoft YaHei,FontSize=19,PrimaryColour=&H00FFFFFF,OutlineColour=&H0028150C,BorderStyle=3,Outline=2,Shadow=0,MarginV=44'
        command(['ffmpeg','-hide_banner','-loglevel','error','-y',
                 '-loop','1','-framerate','10','-i',str(image),'-i',str(audio),
                 '-vf',f"subtitles={subtitles}:force_style='{style}'",
                 '-af','apad','-t',str(seconds),'-c:v','libx264','-preset','veryfast',
                 '-tune','stillimage','-crf','23','-pix_fmt','yuv420p',
                 '-c:a','aac','-b:a','96k','-ar','24000','-ac','1',
                 '-threads','2',str(video)])
        encoded_duration = duration(video)
        chapters.append({'title':slide['title'], 'start':round(elapsed,3),
                         'duration':round(encoded_duration,3)})
        all_cues.extend((a+elapsed,b+elapsed,t) for a,b,t in cues)
        segments.append(video)
        elapsed += encoded_duration
        print(f'Video section {i+1}/{len(slides)} complete', flush=True)
    concat = cache / 'concat.txt'
    concat.write_text(''.join(f"file '{p}'\n" for p in segments))
    video = OUTPUT / 'chapter01-explanation.mp4'
    command(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0',
             '-i',str(concat),'-c','copy','-movflags','+faststart',str(video)])
    (OUTPUT/'chapter01-explanation.vtt').write_text('WEBVTT\n\n'+'\n\n'.join(
        f'{timestamp(a,True)} --> {timestamp(b,True)}\n{t}' for a,b,t in all_cues)+'\n')
    slide_image(slides[0],0,len(slides),args.font,OUTPUT/'poster.jpg')
    (OUTPUT/'chapters.json').write_text(json.dumps(chapters,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'video':str(video),'duration':duration(video),
                      'bytes':video.stat().st_size,'sections':len(slides)},ensure_ascii=False),flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--font',required=True)
    parser.add_argument('--cache',default='/tmp/chapter01-video')
    parser.add_argument('--voice',default='zh-CN-XiaoxiaoNeural')
    parser.add_argument('--rate',default='-5%')
    asyncio.run(main(parser.parse_args()))
