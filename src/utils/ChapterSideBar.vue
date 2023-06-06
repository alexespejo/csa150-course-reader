<script setup>
import SidebarChapters from "./SidebarChapters.vue";
</script>

<template>
 <SidebarChapters heading="Introduction to C++">
  <SidebarChapters heading="A-An Overview of C++" :opened="true">
   <a href="/w01/A#A"><div>An Overview of C++</div></a>
   <a href="/w01/A#B"><div>The C++ Programming Language</div></a>
   <a href="/w01/A#C"><div>Hello World</div></a>
   <a href="/w01/A#D"><div>Source Code</div></a>
   <a href="/w01/A#E"><div>Program Mechanics</div></a>
   <a href="/w01/A#F"><div>The Build Process</div></a>
  </SidebarChapters>
  <SidebarChapters heading="B-The C++ Back Story" :opened="true">
   <a href="/w01/B#A"><div>Early Computing</div></a>
   <a href="/w01/B#B"><div>Machine Language</div></a>
   <a href="/w01/B#C"><div>High-Level Languages</div></a>
   <a href="/w01/B#D"><div>The C Language</div></a>
   <a href="/w01/B#E"><div>Object-Oriented Programming</div></a>
   <a href="/w01/B#F"><div>The C++ Language</div></a>
  </SidebarChapters>
  <SidebarChapters heading="C-Syntax Basics" :opened="true">
   <a href="/w01/C#A"><div>C++ Syntax</div></a>
   <a href="/w01/C#B"><div>The f2c Program</div></a>
   <a href="/w01/C#C"><div>The Standard C++ Library</div></a>
   <a href="/w01/C#D"><div>The main Function</div></a>
   <a href="/w01/C#E"><div>The convert Function</div></a>
  </SidebarChapters>
  <SidebarChapters heading="D-Variables & Values" :opened="true">
   <a href="/w01/D#A"><div>Variables</div></a>
   <a href="/w01/D#B"><div>Definitions & Types</div></a>
   <a href="/w01/D#C"><div>Identifiers & Constants</div></a>
   <a href="/w01/D#D"><div>Initialization</div></a>
   <a href="/w01/D#E"><div>Assignment</div></a>
   <a href="/w01/D#F"><div>Console Output</div></a>
   <a href="/w01/D#G"><div>Console Input</div></a>
  </SidebarChapters>
  <SidebarChapters heading="E-Numbers & Calculations" :opened="true">
   <a href="/w01/E#A"><div>Integers</div></a>
   <a href="/w01/E#B"><div>Signed & Unsigned</div></a>
   <a href="/w01/E#C"><div>Integer Literals</div></a>
   <a href="/w01/E#D"><div>Floating-point Numbers</div></a>
   <a href="/w01/E#E"><div>Floating-point Output</div></a>
   <a href="/w01/E#F"><div>Expressions</div></a>
   <a href="/w01/E#G"><div>Expression Evaluation</div></a>
  </SidebarChapters>
 </SidebarChapters>
</template>

<style lang="scss" scoped>
h2 {
 @apply text-blue-400 pt-3 ml-3 pb-2 text-xs;
}
.collapse-content {
 div {
  @apply text-sm px-0.5 py-1 ml-2;
  a {
   @apply hover:underline hover:text-blue-300;
  }
 }
}
</style>
