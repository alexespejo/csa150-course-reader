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
 <SidebarChapters heading="Functions, Decisions & Strings">
  <SidebarChapters heading="A-Side-Effect Operators" :opened="true">
   <a href="/w02/A#A"><div>Integer Division & Remainders</div></a>
   <a href="/w02/A#B"><div>Assignment Operators</div></a>
   <a href="/w02/A#C"><div>Increment and Decrement</div></a>
   <a href="/w02/A#D"><div>Mixed-type Expressions</div></a>
   <a href="/w02/A#E"><div>Type Casts</div></a>
   <a href="/w02/A#F"><div>Functions</div></a>
   <a href="/w02/A#G"><div>The &lt;cmath &gt; Header</div></a>
  </SidebarChapters>
  <SidebarChapters heading="B-Functions & Decomposition" :opened="true">
   <a href="/w02/B#A"><div>Writing Functions</div></a>
   <a href="/w02/B#B"><div>Function Syntax</div></a>
   <a href="/w02/B#C"><div>The Function Body</div></a>
   <a href="/w02/B#D"><div>Functional Decomposition</div></a>
   <a href="/w02/B#E"><div>Declaring & Defining</div></a>
  </SidebarChapters>
  <SidebarChapters heading="C-Making Decisions" :opened="true">
   <a href="/w02/C#A"><div>Making Decisions</div></a>
   <a href="/w02/C#B"><div>Blocks, Style & Indentation</div></a>
   <a href="/w02/C#C"><div>The bool Data Type</div></a>
   <a href="/w02/C#D"><div>The Relational Operatorrs</div></a>
   <a href="/w02/C#E"><div>The Logical Operators</div></a>
   <a href="/w02/C#F"><div>Multi-way Branching</div></a>
   <a href="/w02/C#G"><div>Nested if Statements</div></a>
  </SidebarChapters>
  <SidebarChapters heading="D-C++ Strings" :opened="true">
   <a href="/w02/D#A"><div>Creating String Object</div></a>
   <a href="/w02/D#B"><div>String Input and Output</div></a>
   <a href="/w02/D#C"><div>Concatenation & Comparison</div></a>
   <a href="/w02/D#D"><div>Mutability & Value Assignment</div></a>
   <a href="/w02/D#E"><div>Member Functions</div></a>
  </SidebarChapters>
  <SidebarChapters heading="E-Processing Strings" :opened="true">
   <a href="/w02/E#A"><div>String Members</div></a>
   <a href="/w02/E#B"><div>Characters</div></a>
   <a href="/w02/E#C"><div>Selecting Characters</div></a>
   <a href="/w02/E#D"><div>Substrings</div></a>
   <a href="/w02/E#E"><div>Searching a String</div></a>
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
   @apply no-underline hover:underline hover:text-blue-500 hover:dark:text-blue-300;
  }
 }
}
</style>
