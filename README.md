### CS150 Course reader project

This project is intended to improve upon the existing [CS150 Course Reader](https://www.occ-cs.com/book-23/)

This new version aims to include various features:

1. Responsive Design (supporting an intuitive layout for small (mobile) and large (desktop) devices)
2. Improved navigation: Full page chapters for faster readings, side bar navigation to jump between sections, searchable content so users can jump between chapters without having to traverse the glossary
3. Most importantly... DARK MODE!

---

### Technology

One major benefit of the old course reader was it's blazingly fast loading time. To emulate such speed we are using the [Astro](https://astro.build/) javascript framework.

Astro allows us to implement new interactive features with javascript without sacrificing speed. Additionally, Astro allows us to implement interactivity using any javascript framework we choose (ex. React, Svelete, Solid, Vue). I have chosen to use the [Vue](https://vuejs.org/) framework.

For our styling, I've chosen TailwindCSS which provides a faster and "creative" developer experience especially when working with the existing css of the legacy course reader. However, when writing our own CSS I have included the SASS/SCSS preprocesser (mainly for nested styling).

![Responsive Layout sm-md](./public/images/ResponsiveLayout.png)
![Responsive Layout large](./public/images/ResponsiveDesign-lg.png)
