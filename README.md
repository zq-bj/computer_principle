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
│   │   ├── 01_计算机系统概述/
│   │   │   ├── 01_1_冯诺依曼思想.md
│   │   │   ├── 01_2_程序的开发和执行过程.md
│   │   │   ├── 01_3_计算机系统层次结构.md
│   │   │   └── 01_4_计算机性能评价.md
│   │   ├── 02_数据表示和运算/
│   │   │   ├── 02_1_数值数据的表示.md
│   │   │   ├── 02_2_非数值数据的表示.md
│   │   │   ├── 02_3_数据的存放.md
│   │   │   └── 02_4_数据的运算.md
│   │   ├── 03_程序转换与机器级表示/
│   │   ├── 04_可执行文件的生成与加载/
│   │   ├── 05_程序的存储访问/
│   │   └── 06_IO操作的实现/
│   ├── progress.md         # 学习进度
│   ├── _posts/             # 博客文章
│   └── reading/            # 读书笔记
├── exercises/              # 练习题
├── exams/                  # 历年真题
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

网站地址：https://zq-bj.github.io/computer_principle/

在仓库 Settings → Pages 中选择 GitHub Actions 作为发布来源。推送到 GitHub 的 `main` 分支后，工作流自动安装依赖、构建并部署网站，也可在 Actions 页面手动触发。

本地开发默认使用根路径 `/`；GitHub Pages 构建通过 `DOCS_BASE=/computer_principle/` 设置仓库子路径。可在本地执行相同构建：

```bash
DOCS_BASE=/computer_principle/ pnpm docs:build
```

构建产物位于 `src/.vuepress/dist`，由工作流发布，无需提交生成文件。

## 章节顺序
1. 第一章 计算机系统概述
2. 第二章 数据表示和运算
3. 第三章 程序转换与机器级表示
4. 第四章 可执行文件的生成与加载
5. 第五章 程序的存储访问
6. 第六章 IO操作的实现
