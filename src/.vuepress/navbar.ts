import type { NavbarConfig } from "vuepress-theme-hope";

export const navbar: NavbarConfig = [
  {
    text: "学习笔记",
    link: "/computer_principle/",
    children: [
      {
        text: "第一章 计算机系统概述",
        children: [
          {
            text: "第一章视频讲解",
            link: "/computer_principle/01_计算机系统概述/01_计算机系统概述",
          },
          {
            text: "1.1 冯诺依曼结构计算机特点",
            link: "/computer_principle/01_计算机系统概述/01_1_冯诺依曼思想",
          },
          {
            text: "1.2 程序的开发和执行过程",
            link: "/computer_principle/01_计算机系统概述/01_2_程序的开发和执行过程",
          },
          {
            text: "1.3 计算机系统层次结构",
            link: "/computer_principle/01_计算机系统概述/01_3_计算机系统层次结构",
          },
          {
            text: "1.4 计算机性能评价",
            link: "/computer_principle/01_计算机系统概述/01_4_计算机性能评价",
          },
          {
            text: "1.5 作业",
            link: "/computer_principle/01_计算机系统概述/01_5_作业",
          },
        ],
      },
      {
        text: "第二章 数据表示和运算",
        children: [
          {
            text: "2.1 进位计数制",
            link: "/computer_principle/02_数据表示和运算/02_1_进位计数制",
          },
          {
            text: "2.2 定点数的编码规则",
            link: "/computer_principle/02_数据表示和运算/02_2_定点数的编码规则",
          },
          {
            text: "2.3 浮点数与数值类型转换",
            link: "/computer_principle/02_数据表示和运算/02_3_浮点数与数值类型转换",
          },
          {
            text: "2.4 数据宽度与存放",
            link: "/computer_principle/02_数据表示和运算/02_4_数据宽度与存放",
          },
          {
            text: "2.5 作业",
            link: "/computer_principle/02_数据表示和运算/02_5_作业",
          },
        ],
      },
      {
        text: "第三章 程序转换与机器级表示",
        link: "/computer_principle/03_程序转换与机器级表示/03_程序转换与机器级表示",
      },
      {
        text: "第四章 可执行文件的生成与加载",
        link: "/computer_principle/04_可执行文件的生成与加载/04_可执行文件的生成与加载",
      },
      {
        text: "第五章 程序的存储访问",
        link: "/computer_principle/05_程序的存储访问/05_程序的存储访问",
      },
      {
        text: "第六章 I/O操作的实现",
        link: "/computer_principle/06_IO操作的实现/06_IO操作的实现",
      },
    ],
  },
  {
    text: "练习题",
    link: "/exercises/",
  },
  {
    text: "历年真题",
    link: "/exams/",
  },
  {
    text: "学习进度",
    link: "/progress",
  },
];
