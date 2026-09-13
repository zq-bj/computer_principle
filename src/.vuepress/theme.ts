import { hopeTheme } from "vuepress-theme-hope";
import { navbar, sidebar } from "./navbar.js";

export default hopeTheme({
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
    slimsearch: true,
    comment: {
      provider: "giscus",
      repo: "your-username/computer-principle",
      repoId: "your-repo-id",
      category: "Announcements",
      categoryId: "your-category-id",
    },
  },
});
