import { defineUserConfig } from "vuepress";
import { viteBundler } from "@vuepress/bundler-vite";
import { hopeTheme } from "vuepress-theme-hope";
import { navbar } from "./navbar.js";
import { sidebar } from "./sidebar.js";

export default defineUserConfig({
  base: "/",
  bundler: viteBundler(),

  locales: {
    "/": {
      lang: "zh-CN",
      title: "计算机系统原理",
      description: "北京自考 - 计算机系统原理学习笔记",
    },
  },

  theme: hopeTheme({
    locales: {
      "/": {
        navbar: navbar,
        sidebar: sidebar,
        footer: "计算机系统原理 - 北京自考",
        displayFooter: true,
      },
    },
    themeColor: {
      pink: "#ff6b9d",
      blue: "#49b6ff",
    },
    dark: "toggle",
    logo: "/logo.svg",
    repo: "your-username/computer-principle",
    docsDir: "src",
    sidebarSorting: "order",
    plugins: {
      mdEnhance: {
        mermaid: true,
      },
    },
  }),

  markdown: {
    lineNumbers: true,
  },
});
