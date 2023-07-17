<script setup>
import SidebarChapters from "./SidebarChapters.vue";
import SidebarChapterHeading from "./SidebarChapterHeading.vue";
</script>
<template>
 <SidebarChapters heading="Introduction to C++">
  <SidebarChapterHeading heading="A-An Overview of C++" :opened="true">
   <a href="/w01/A#A"><span>An Overview of C++</span></a>
   <a href="/w01/A#B"><span>The C++ Programming Language</span></a>
   <a href="/w01/A#C"><span>Hello World</span></a>
   <a href="/w01/A#D"><span>Source Code</span></a>
   <a href="/w01/A#E"><span>Program Mechanics</span></a>
   <a href="/w01/A#F"><span>The Build Process</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="B-The C++ Back Story" :opened="true">
   <a href="/w01/B#A"><span>Early Computing</span></a>
   <a href="/w01/B#B"><span>Machine Language</span></a>
   <a href="/w01/B#C"><span>High-Level Languages</span></a>
   <a href="/w01/B#D"><span>The C Language</span></a>
   <a href="/w01/B#E"><span>Object-Oriented Programming</span></a>
   <a href="/w01/B#F"><span>The C++ Language</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="C-Syntax Basics" :opened="true">
   <a href="/w01/C#A"><span>C++ Syntax</span></a>
   <a href="/w01/C#B"><span>The f2c Program</span></a>
   <a href="/w01/C#C"><span>The Standard C++ Library</span></a>
   <a href="/w01/C#D"><span>The main Function</span></a>
   <a href="/w01/C#E"><span>The convert Function</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="D-Variables & Values" :opened="true">
   <a href="/w01/D#A"><span>Variables</span></a>
   <a href="/w01/D#B"><span>Definitions & Types</span></a>
   <a href="/w01/D#C"><span>Identifiers & Constants</span></a>
   <a href="/w01/D#D"><span>Initialization</span></a>
   <a href="/w01/D#E"><span>Assignment</span></a>
   <a href="/w01/D#F"><span>Console Output</span></a>
   <a href="/w01/D#G"><span>Console Input</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="E-Numbers & Calculations" :opened="true">
   <a href="/w01/E#A"><span>Integers</span></a>
   <a href="/w01/E#B"><span>Signed & Unsigned</span></a>
   <a href="/w01/E#C"><span>Integer Literals</span></a>
   <a href="/w01/E#D"><span>Floating-point Numbers</span></a>
   <a href="/w01/E#E"><span>Floating-point Output</span></a>
   <a href="/w01/E#F"><span>Expressions</span></a>
   <a href="/w01/E#G"><span>Expression Evaluation</span></a>
  </SidebarChapterHeading>
 </SidebarChapters>
 <SidebarChapters heading="Functions, Decisions & Strings">
  <SidebarChapterHeading heading="A-Side-Effect Operators" :opened="true">
   <a href="/w02/A#A"><span>Integer Division & Remainders</span></a>
   <a href="/w02/A#B"><span>Assignment Operators</span></a>
   <a href="/w02/A#C"><span>Increment and Decrement</span></a>
   <a href="/w02/A#D"><span>Mixed-type Expressions</span></a>
   <a href="/w02/A#E"><span>Type Casts</span></a>
   <a href="/w02/A#F"><span>Functions</span></a>
   <a href="/w02/A#G"><span>The &lt;cmath &gt; Header</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="B-Functions & Decomposition" :opened="true">
   <a href="/w02/B#A"><span>Writing Functions</span></a>
   <a href="/w02/B#B"><span>Function Syntax</span></a>
   <a href="/w02/B#C"><span>The Function Body</span></a>
   <a href="/w02/B#D"><span>Functional Decomposition</span></a>
   <a href="/w02/B#E"><span>Declaring & Defining</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="C-Making Decisions" :opened="true">
   <a href="/w02/C#A"><span>Making Decisions</span></a>
   <a href="/w02/C#B"><span>Blocks, Style & Indentation</span></a>
   <a href="/w02/C#C"><span>The bool Data Type</span></a>
   <a href="/w02/C#D"><span>The Relational Operatorrs</span></a>
   <a href="/w02/C#E"><span>The Logical Operators</span></a>
   <a href="/w02/C#F"><span>Multi-way Branching</span></a>
   <a href="/w02/C#G"><span>Nested if Statements</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="D-C++ Strings" :opened="true">
   <a href="/w02/D#A"><span>Creating String Object</span></a>
   <a href="/w02/D#B"><span>String Input and Output</span></a>
   <a href="/w02/D#C"><span>Concatenation & Comparison</span></a>
   <a href="/w02/D#D"><span>Mutability & Value Assignment</span></a>
   <a href="/w02/D#E"><span>Member Functions</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="E-Processing Strings" :opened="true">
   <a href="/w02/E#A"><span>String Members</span></a>
   <a href="/w02/E#B"><span>Characters</span></a>
   <a href="/w02/E#C"><span>Selecting Characters</span></a>
   <a href="/w02/E#D"><span>Substrings</span></a>
   <a href="/w02/E#E"><span>Searching a String</span></a>
  </SidebarChapterHeading>
 </SidebarChapters>
 <SidebarChapters heading="Programming with Loops">
  <SidebarChapterHeading heading="A-Reference Types" :opened="true">
   <a href="/w03/A#A"><span>References</span></a>
   <a href="/w03/A#B"><span>Conversions & Const-ref</span></a>
   <a href="/w03/A#C"><span>Reference Parameters</span></a>
   <a href="/w03/A#D"><span>String Value Parameters</span></a>
   <a href="/w03/A#E"><span>String Reference Parameters</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="B-Introducing Loops" :opened="true">
   <a href="/w03/B#A"><span>Introducing Loops</span></a>
   <a href="/w03/B#B"><span>Guarded & Unguarded Loops</span></a>
   <a href="/w03/B#C"><span>Classifying Loops</span></a>
   <a href="/w03/B#D"><span>Indefinite Loop Categories</span></a>
   <a href="/w03/B#E"><span>Range-based Loops</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="C-Definite Loops with For" :opened="true">
   <a href="/w03/C#A"><span>Definite Loops with for</span></a>
   <a href="/w03/C#B"><span>Sequences & Symmetric Bounds</span></a>
   <a href="/w03/C#C"><span>Processing Strings</span></a>
   <a href="/w03/C#D"><span>Some Bad Habits</span></a>
   <a href="/w03/C#E"><span>Hands On: Counting Vowels</span></a>
   <a href="/w03/C#F"><span>Hands On: Counting Substrings</span></a>
   <a href="/w03/C#G"><span>More Efficient Substrings</span></a>
   <a href="/w03/C#H"><span>Substrings Redux</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="D-How to Write Loops" :opened="true">
   <a href="/w03/D#A"><span>Goal, Bounds & Plan</span></a>
   <a href="/w03/D#B"><span>Implement the Plan</span></a>
   <a href="/w03/D#C"><span>The Loop Bounds</span></a>
   <a href="/w03/D#D"><span>The Bounds Precondition</span></a>
   <a href="/w03/D#E"><span>Advancing the Loop</span></a>
   <a href="/w03/D#F"><span>The Loop Goal</span></a>
   <a href="/w03/D#G"><span>Loop Operations</span></a>
   <a href="/w03/D#H"><span>The Loop Postcondition</span></a>
   <a href="/w03/D#I"><span>Loop Guards</span></a>
   <a href="/w03/D#J"><span>Necessary & Intentional</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="E-Sentinel Loop Patterns" :opened="true">
   <a href="/w03/E#A"><span>Sentinel Loop Patters</span></a>
   <a href="/w03/E#B"><span>The Primed Loop Pattern</span></a>
   <a href="/w03/E#C"><span>The Loop-and-a-half Pattern</span></a>
   <a href="/w03/E#D"><span>The Flag-controlled Pattern</span></a>
   <a href="/w03/E#E"><span>Validating Data</span></a>
  </SidebarChapterHeading>
 </SidebarChapters>
 <SidebarChapters heading="Function Libraries">
  <SidebarChapterHeading heading="A-Library Mechanics" :opened="true">
   <a href="/w04/A#A"><span>Library Mechanics</span></a>
   <a href="/w04/A#B"><span>Separate Compilation</span></a>
   <a href="/w04/A#C"><span>The Client or Test Program</span></a>
   <a href="/w04/A#D"><span>The Interface or Header File</span></a>
   <a href="/w04/A#E"><span>Adding the Prototypes</span></a>
   <a href="/w04/A#F"><span>Library Types in Interfaces</span></a>
   <a href="/w04/A#G"><span>The Implementation File</span></a>
   <a href="/w04/A#H"><span>Stubbing the Implementation</span></a>
   <a href="/w04/A#I"><span>The Make File</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading
   heading="B-Documentation & Implementation"
   :opened="true"
  >
   <a href="/w04/B#A"><span>Documenting the Interface</span></a>
   <a href="/w04/B#B"><span>Planning & Implementation</span></a>
   <a href="/w04/B#C"><span>The while Loop</span></a>
   <a href="/w04/B#D"><span>Limit Bounds</span></a>
   <a href="/w04/B#E"><span>Running Doxygen</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading
   heading="C-Overloading & Default Arguments"
   :opened="true"
  >
   <a href="/w04/C#A"><span>Overloaded Functions</span></a>
   <a href="/w04/C#B"><span>Overload Resolution</span></a>
   <a href="/w04/C#C"><span>Default Arguments</span></a>
   <a href="/w04/C#D"><span>Default Argument Rules</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="D-Data Flows" :opened="true">
   <a href="/w04/D#A"><span>Data Flows</span></a>
   <a href="/w04/D#B"><span>Output Parameters</span></a>
   <a href="/w04/D#C"><span>Input and Output Parameters</span></a>
   <a href="/w04/D#D"><span>Input-Output Parameters</span></a>
   <a href="/w04/D#E"><span>Data Flow Checklists</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="E-More Selections & Iteration" :opened="true">
   <a href="/w04/E#A"><span>More Selections & Iteration</span></a>
   <a href="/w04/E#B"><span>The switch Statement</span></a>
   <a href="/w04/E#C"><span>More on switch</span></a>
   <a href="/w04/E#D"><span>The Conditional Operator</span></a>
   <a href="/w04/E#E"><span>A Hasty Loop</span></a>
   <a href="/w04/E#F"><span>Confirmation Loops</span></a>
  </SidebarChapterHeading>
 </SidebarChapters>
 <SidebarChapters heading="Recursion, Streams & Filters">
  <SidebarChapterHeading heading="A-Introducing Recursion" :opened="true">
   <a href="/w05/A#A"><span>Introducing Recursion</span></a>
   <a href="/w05/A#B"><span>The Factorial Function</span></a>
   <a href="/w05/A#C"><span>A Recursive Example</span></a>
   <a href="/w05/A#D"><span>The Recursive Leap of Faith</span></a>
   <a href="/w05/A#E"><span>The Fibonacci Sequence</span></a>
   <a href="/w05/A#F"><span>Recursive Efficiency</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="B-Efficient Recursion" :opened="true">
   <a href="/w05/B#A"><span>Efficient Recursion</span></a>
   <a href="/w05/B#B"><span>Wrappers & Helpers</span></a>
   <a href="/w05/B#C"><span>Checking Palindromes</span></a>
   <a href="/w05/B#D"><span>Palindrome Efficiency</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="C-Applying Recursion" :opened="true">
   <a href="/w05/C#A"><span>A Recursion Checklist I</span></a>
   <a href="/w05/C#B"><span>A Recursion Checklist II</span></a>
   <a href="/w05/C#C"><span>Code Step-by-Step</span></a>
   <a href="/w05/C#D"><span>Solving the Problem I</span></a>
   <a href="/w05/C#E"><span>Solving the Problem II</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="D-Streams & Redirection" :opened="true">
   <a href="/w05/D#A"><span>The Standard Streams</span></a>
   <a href="/w05/D#B"><span>The cat Filter</span></a>
   <a href="/w05/D#C"><span>Input Redirection</span></a>
   <a href="/w05/D#D"><span>Output Redirection</span></a>
   <a href="/w05/D#E"><span>Error Redirection</span></a>
   <a href="/w05/D#F"><span>Pipes & Pipelines</span></a>
   <a href="/w05/D#G"><span>Built-in Filters</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="E-Filters" :opened="true">
   <a href="/w05/E#A"><span>Process Filters</span></a>
   <a href="/w05/E#B"><span>State Filters</span></a>
   <a href="/w05/E#C"><span>Your First Filter</span></a>
   <a href="/w05/E#D"><span>Data Loops</span></a>
   <a href="/w05/E#E"><span>More on Streams</span></a>
  </SidebarChapterHeading>
 </SidebarChapters>
 <SidebarChapters heading="Files, String Streams & Errors">
  <SidebarChapterHeading heading="A-Processing Files" :opened="true">
   <a href="/w06/A#A"><span>The Stream Classes</span></a>
   <a href="/w06/A#B"><span>UML Diagrams</span></a>
   <a href="/w06/A#C"><span>Easy File I/O</span></a>
   <a href="/w06/A#D"><span>Processing Lines</span></a>
   <a href="/w06/A#E"><span>Processing Tokens</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="B-Validating Data" :opened="true">
   <a href="/w06/B#A"><span>Applied File I/O</span></a>
   <a href="/w06/B#B"><span>Stub the Function</span></a>
   <a href="/w06/B#C"><span>Searching & Numbering</span></a>
   <a href="/w06/B#D"><span>Validating Data</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="C-String Streams" :opened="true">
   <a href="/w06/C#A"><span>String Streams</span></a>
   <a href="/w06/C#B"><span>The format Function</span></a>
   <a href="/w06/C#C"><span>Input String Streams</span></a>
   <a href="/w06/C#D"><span>An Input Stream Exercise</span></a>
   <a href="/w06/C#E"><span>The Arguments</span></a>
   <a href="/w06/C#F"><span>The Longest Line</span></a>
   <a href="/w06/C#G"><span>Counting the Lines</span></a>
   <a href="/w06/C#H"><span>Processing the Tokens</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="D-Conditional Compilation" :opened="true">
   <a href="/w06/D#A"><span>Conversion Functions</span></a>
   <a href="/w06/D#B"><span>Using the Functions</span></a>
   <a href="/w06/D#C"><span>Stub the Replacements</span></a>
   <a href="/w06/D#D"><span>Using #define</span></a>
   <a href="/w06/D#E"><span>Conditional Compilation</span></a>
   <a href="/w06/D#F"><span>Predefined Symbols</span></a>
   <a href="/w06/D#G"><span>Comparing the Results</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="E-Errors & Assertions" :opened="true">
   <a href="/w06/E#A"><span>Handling Errors</span></a>
   <a href="/w06/E#B"><span>The Terminator</span></a>
   <a href="/w06/E#C"><span>Using assert</span></a>
   <a href="/w06/E#D"><span>More Assertions</span></a>
   <a href="/w06/E#E"><span>Completion Codes</span></a>
   <a href="/w06/E#F"><span>Error Flags</span></a>
  </SidebarChapterHeading>
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
   @apply no-underline hover:underline hover:text-blue-500 hover:dark:text-blue-300 hover:bg-blue-800;
  }
 }
}
</style>
