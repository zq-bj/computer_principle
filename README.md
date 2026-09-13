# 计算机系统原理 - 北京自考

## 项目信息
- **课程名称**: 计算机系统原理
- **考试类型**: 北京自考
- **国家代码**: 13015
- **学分**: 4学分（学位课程）
- **教材**: 《计算机系统原理》袁春风，机械工业出版社，2023年版
- **学习目的**: 通过考试

## 项目说明
本项目用于学习计算机系统原理课程，为北京高等教育自学考试（国家代码13015）做准备。

## 技术栈
- **框架**: VuePress 2 + vuepress-theme-hope
- **内容格式**: Markdown
- **部署方式**: GitHub Pages / Vercel
- **开发环境**: Node.js + pnpm

## 目录结构
```
├── src/                    # 源代码目录
│   ├── .vuepress/          # VuePress配置文件
│   │   ├── config.ts       # 网站配置
│   │   ├── navbar.ts       # 导航栏配置
│   │   ├── sidebar.ts      # 侧边栏配置
│   │   └── theme.ts        # 主题配置
│   ├── computer_principle/ # 学习笔记
│   │   ├── 01_计算机系统概述.md
│   │   ├── 02_数据表示和运算.md
│   │   ├── 03_程序转换与机器级表示.md
│   │   ├── 04_可执行文件的生成与加载.md
│   │   ├── 05_程序的存储访问.md
│   │   └── 06_IO操作的实现.md
│   ├── _posts/             # 博客文章
│   └── reading/            # 读书笔记
├── exercises/              # 练习题
├── exams/                  # 历年真题
├── PROGRESS.md             # 学习进度
└── package.json            # 项目依赖配置
```

## 学习资源
- 教材和参考书
- 历年真题和模拟题
- 视频教程（用户自备）

## 学习方法
1. 看完视频后复述知识点
2. 我出题测试巩固
3. 遇到疑问随时答疑
4. 整理笔记保存复习

## 开发命令
```bash
# 安装依赖
pnpm install

# 本地开发
pnpm docs:dev

# 构建静态网站
pnpm docs:build

# 清理缓存
pnpm docs:clean
```

## 笔记格式规范
每个笔记文件需要包含frontmatter：
```markdown
---
title: 章节标题
date: YYYY-MM-DD
tags: [计算机原理, 章节名称]
order: 章节序号
---

# 章节内容
```

## 部署说明
1. 推送到GitHub仓库
2. GitHub Actions自动构建
3. 部署到GitHub Pages
4. 访问地址：https://your-username.github.io/computer-principle/

## 章节顺序
1. 第一章 计算机系统概述
2. 第二章 数据表示和运算
3. 第三章 程序转换与机器级表示
4. 第四章 可执行文件的生成与加载
5. 第五章 程序的存储访问
6. 第六章 IO操作的实现
