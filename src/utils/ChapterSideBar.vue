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
 <SidebarChapters heading="Exceptions, Templates & Structures">
  <SidebarChapterHeading heading="A-Exception Handling" :opened="true">
   <a href="/w07/A#A"><span>Exception Handling</span></a>
   <a href="/w07/A#B"><span>Throwing Exceptions</span></a>
   <a href="/w07/A#C"><span>What Should You Throw?</span></a>
   <a href="/w07/A#D"><span>The try and catch Blocks</span></a>
   <a href="/w07/A#E"><span>Other catch Blocks</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="B-Templates" :opened="true">
   <a href="/w07/B#A"><span>The to_string Functions</span></a>
   <a href="/w07/B#B"><span>Function Templates</span></a>
   <a href="/w07/B#C"><span>Template Instantiation</span></a>
   <a href="/w07/B#D"><span>Template Argument Deduction</span></a>
   <a href="/w07/B#E"><span>Multiple Template Arguments</span></a>
   <a href="/w07/B#F"><span>Explicit Template Arguments</span></a>
   <a href="/w07/B#G"><span>Inferred Return Types</span></a>
   <a href="/w07/B#H"><span>Templates & Overloading</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="C-Structured Types" :opened="true">
   <a href="/w07/C#A"><span>Structured Types</span></a>
   <a href="/w07/C#B"><span>Structure Definitions</span></a>
   <a href="/w07/C#C"><span>Structure Variables</span></a>
   <a href="/w07/C#D"><span>Initialization</span></a>
   <a href="/w07/C#E"><span>Member Access</span></a>
   <a href="/w07/C#F"><span>Aggregate Operations</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="D-Structures & Functions" :opened="true">
   <a href="/w07/D#A"><span>Structure Arguments</span></a>
   <a href="/w07/D#B"><span>By-Value or By-Reference</span></a>
   <a href="/w07/D#C"><span>A Compare Function</span></a>
   <a href="/w07/D#D"><span>Returning Structures</span></a>
   <a href="/w07/D#E"><span>Structured Bindings</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="E-Enumerated Types" :opened="true">
   <a href="/w07/E#A"><span>Enumerated Types</span></a>
   <a href="/w07/E#B"><span>Defining Enumerated Types</span></a>
   <a href="/w07/E#C"><span>Enumerated Variables</span></a>
   <a href="/w07/E#D"><span>Enumerated Output</span></a>
   <a href="/w07/E#E"><span>Enumerated Input</span></a>
  </SidebarChapterHeading>
 </SidebarChapters>
 <SidebarChapters heading="Vectors, Memory, Pointers & Graphics">
  <SidebarChapterHeading heading="A-The vector Type" :opened="true">
   <a href="/w08/A#A"><span>Why Vectors?</span></a>
   <a href="/w08/A#B"><span>Meet the vector</span></a>
   <a href="/w08/A#C"><span>Vector Variables</span></a>
   <a href="/w08/A#D"><span>Vector Initialization</span></a>
   <a href="/w08/A#E"><span>Element Access</span></a>
   <a href="/w08/A#F"><span>Range Checking</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="B-Processing Vectors" :opened="true">
   <a href="/w08/B#A"><span>Growing & Shrinking</span></a>
   <a href="/w08/B#B"><span>Vectors & Loops</span></a>
   <a href="/w08/B#C"><span>Common Algorithms</span></a>
   <a href="/w08/B#D"><span>Counting Algorithms</span></a>
   <a href="/w08/B#E"><span>Cumulative Algorithms</span></a>
   <a href="/w08/B#F"><span>Extreme Values</span></a>
   <a href="/w08/B#G"><span>Modifying Algorithms</span></a>
   <a href="/w08/B#H"><span>Filling & Shuffling</span></a>
   <a href="/w08/B#I"><span>Vectors & Functions</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="C-Memory & Addresses" :opened="true">
   <a href="/w08/C#A"><span>Memory & Addresses</span></a>
   <a href="/w08/C#B"><span>Naming Concepts</span></a>
   <a href="/w08/C#C"><span>Global Variables</span></a>
   <a href="/w08/C#D"><span>Local Variables</span></a>
   <a href="/w08/C#E"><span>Characteristics of Variables</span></a>
   <a href="/w08/C#F"><span>The sizeof Operator</span></a>
   <a href="/w08/C#G"><span>The Address Operator</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="D-Pointers" :opened="true">
   <a href="/w08/D#A"><span>Pointers</span></a>
   <a href="/w08/D#B"><span>Defining Pointers</span></a>
   <a href="/w08/D#C"><span>Initializing Pointers</span></a>
   <a href="/w08/D#D"><span>Dereferencing Pointers</span></a>
   <a href="/w08/D#E"><span>Pointer Assignment</span></a>
   <a href="/w08/D#F"><span>The "null" Pointer</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="E-Pointers & Graphics" :opened="true">
   <a href="/w08/E#A"><span>Digital Images</span></a>
   <a href="/w08/E#B"><span>RGB Colors</span></a>
   <a href="/w08/E#C"><span>The RGB Explorer</span></a>
   <a href="/w08/E#D"><span>Digital Images in C++</span></a>
   <a href="/w08/E#E"><span>Loading an Image</span></a>
   <a href="/w08/E#F"><span>More on Loading an Image</span></a>
   <a href="/w08/E#G"><span>Saving an Image</span></a>
   <a href="/w08/E#H"><span>Changing the Format</span></a>
  </SidebarChapterHeading>
 </SidebarChapters>
 <SidebarChapters heading="Pointers, Arrays & Algorithms">
  <SidebarChapterHeading heading="A-Image Filters" :opened="true">
   <a href="/w09/A#A"><span>Digital Filters</span></a>
   <a href="/w09/A#B"><span>Address Arithmetic</span></a>
   <a href="/w09/A#C"><span>Iterator Loops</span></a>
   <a href="/w09/A#D"><span>The Darken Filter</span></a>
   <a href="/w09/A#E"><span>Dealing with Channels</span></a>
   <a href="/w09/A#F"><span>State Filters</span></a>
   <a href="/w09/A#G"><span>Pointers & Structures</span></a>
   <a href="/w09/A#H"><span>Using reinterpret_cast</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="B-Introducing Arrays" :opened="true">
   <a href="/w09/B#A"><span>Introducing Arrays</span></a>
   <a href="/w09/B#B"><span>Array vs. vector</span></a>
   <a href="/w09/B#C"><span>Defining Arrays</span></a>
   <a href="/w09/B#D"><span>Array Initialization</span></a>
   <a href="/w09/B#E"><span>The Allocated Size</span></a>
   <a href="/w09/B#F"><span>Array Selection</span></a>
   <a href="/w09/B#G"><span>Characteristics of Arrays</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading
   heading="C-Pointers, Arrays & Functions"
   :opened="true"
  >
   <a href="/w09/C#A"><span>Pointers & Arrays</span></a>
   <a href="/w09/C#B"><span>Pointer Arithmetic & Arrays</span></a>
   <a href="/w09/C#C"><span>Dereferencing Arrays</span></a>
   <a href="/w09/C#D"><span>Arrays & Functions</span></a>
   <a href="/w09/C#E"><span>Decaying Arrays</span></a>
   <a href="/w09/C#F"><span>Arrays & Const</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="D-Arrays & Loops" :opened="true">
   <a href="/w09/D#A"><span>Arrays and Loops</span></a>
   <a href="/w09/D#B"><span>Counter-Controlled Loops</span></a>
   <a href="/w09/D#C"><span>Sentinel Loops</span></a>
   <a href="/w09/D#D"><span>Iterator Loops</span></a>
   <a href="/w09/D#E"><span>A C++ Idiom</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="E-Arrays & Algorithms" :opened="true">
   <a href="/w09/E#A"><span>Arrays and Algorithms</span></a>
   <a href="/w09/E#B"><span>Counting Algorithms</span></a>
   <a href="/w09/E#C"><span>Cumulative Algorithms</span></a>
   <a href="/w09/E#D"><span>Extreme Values</span></a>
   <a href="/w09/E#E"><span>Returning a Pointer</span></a>
   <a href="/w09/E#F"><span>Returning an Index</span></a>
   <a href="/w09/E#G"><span>The Fencepost Algorithm</span></a>
   <a href="/w09/E#H"><span>A Reverse Fencepost</span></a>
  </SidebarChapterHeading>
 </SidebarChapters>
 <SidebarChapters heading="C-Strings, Partially-Filled & 2D Arrays">
  <SidebarChapterHeading heading="A-Searching Algorithms" :opened="true">
   <a href="/w10/A#A"><span>Searching Algorithms</span></a>
   <a href="/w10/A#B"><span>The Starter Code</span></a>
   <a href="/w10/A#C"><span>The find() Function</span></a>
   <a href="/w10/A#D"><span>Linear Search</span></a>
   <a href="/w10/A#E"><span>Linear Search Efficiency</span></a>
   <a href="/w10/A#F"><span>Improving Linear Search</span></a>
   <a href="/w10/A#G"><span>Binary Search</span></a>
   <a href="/w10/A#H"><span>Implementing Binary Search</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="B-Partially-Filled Arrays" :opened="true">
   <a href="/w10/B#A"><span>An Array Example</span></a>
   <a href="/w10/B#B"><span>Appending Elements</span></a>
   <a href="/w10/B#C"><span>Traversing the Array</span></a>
   <a href="/w10/B#D"><span>Inserting Elements</span></a>
   <a href="/w10/B#E"><span>Applying the Algorithm</span></a>
   <a href="/w10/B#F"><span>Removing Elements</span></a>
   <a href="/w10/B#G"><span>Removing Multiple Elements</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="C-2D Arrays" :opened="true">
   <a href="/w10/C#A"><span>2D Arrays</span></a>
   <a href="/w10/C#B"><span>Row Major Order</span></a>
   <a href="/w10/C#C"><span>2D Array Initialization</span></a>
   <a href="/w10/C#D"><span>2D Arrays & Functions</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="D-C-Style Strings" :opened="true">
   <a href="/w10/D#A"><span>C-Style Strings</span></a>
   <a href="/w10/D#B"><span>C-String Basics</span></a>
   <a href="/w10/D#C"><span>Array-based C-Strings</span></a>
   <a href="/w10/D#D"><span>Pointer-based C-Strings</span></a>
   <a href="/w10/D#E"><span>C++ Strings vs. C-Strings</span></a>
   <a href="/w10/D#F"><span>C-String Assignment</span></a>
   <a href="/w10/D#G"><span>The strncpy Function</span></a>
   <a href="/w10/D#H"><span>The strcat Functions</span></a>
   <a href="/w10/D#I"><span>Comparing C-Strings</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="E-Writing C-String Functions" :opened="true">
   <a href="/w10/E#A"><span>The strlen Function</span></a>
   <a href="/w10/E#B"><span>The strcpy Function</span></a>
   <a href="/w10/E#C"><span>The strcmp Function</span></a>
   <a href="/w10/E#D"><span>Writing Your Own Functions</span></a>
   <a href="/w10/E#E"><span>Find First</span></a>
   <a href="/w10/E#F"><span>Find Last</span></a>
   <a href="/w10/E#G"><span>Find First of Any</span></a>
   <a href="/w10/E#H"><span>Finding Substrings</span></a>
  </SidebarChapterHeading>
 </SidebarChapters>
 <SidebarChapters heading="Dynamic Memory & Smart Pointers">
  <SidebarChapterHeading heading="A-The Command Line" :opened="true">
   <a href="/w11/A#A"><span>The Shell</span></a>
   <a href="/w11/A#B"><span>The Command Line</span></a>
   <a href="/w11/A#C"><span>Command-Line Arguments</span></a>
   <a href="/w11/A#D"><span>Using Command-Line Arguments</span></a>
   <a href="/w11/A#E"><span>Traversing the Arguments</span></a>
   <a href="/w11/A#F"><span>Converting Arguments</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="B-Dynamic Memory" :opened="true">
   <a href="/w11/B#A"><span>Introducing the Heap</span></a>
   <a href="/w11/B#B"><span>Stack vs. Heap</span></a>
   <a href="/w11/B#C"><span>The new Operator</span></a>
   <a href="/w11/B#D"><span>Dyanmic Arrays</span></a>
   <a href="/w11/B#E"><span>Dynamic Objects</span></a>
   <a href="/w11/B#F"><span>Freeing Memory</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="C-Smart Pointers" :opened="true">
   <a href="/w11/C#A"><span>Memory Management</span></a>
   <a href="/w11/C#B"><span>Memory Leaks</span></a>
   <a href="/w11/C#C"><span>Dangling Pointers</span></a>
   <a href="/w11/C#D"><span>Double Deletes</span></a>
   <a href="/w11/C#E"><span>Smart Pointers</span></a>
   <a href="/w11/C#F"><span>Shared Pointers</span></a>
   <a href="/w11/C#G"><span>Unique Pointers</span></a>
   <a href="/w11/C#H"><span>Smart Pointers & Functions</span></a>
   <a href="/w11/C#I"><span>Unique Pointers and Containers</span></a>
   <a href="/w11/C#J"><span>Unique Pointers and Dynamic Arrays</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="D-The Problem with Structures" :opened="true">
   <a href="/w11/D#A"><span>The Iron Age</span></a>
   <a href="/w11/D#B"><span>User-Defined Types</span></a>
   <a href="/w11/D#C"><span>Object-Based Programming</span></a>
   <a href="/w11/D#D"><span>Time as a Structure</span></a>
   <a href="/w11/D#E"><span>Type Invariants</span></a>
   <a href="/w11/D#F"><span>A Scenario</span></a>
   <a href="/w11/D#G"><span>The Problem</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="E-Member Functions" :opened="true">
   <a href="/w11/E#A"><span>Information Hiding</span></a>
   <a href="/w11/E#B"><span>The Public Interface</span></a>
   <a href="/w11/E#C"><span>Member Functions</span></a>
   <a href="/w11/E#D"><span>Proving the Interface</span></a>
   <a href="/w11/E#E"><span>The Implementation File</span></a>
   <a href="/w11/E#F"><span>Implementing Member Functions</span></a>
  </SidebarChapterHeading>
 </SidebarChapters>
 <SidebarChapters heading="Object Based Programming with Classes">
  <SidebarChapterHeading heading="A-Objects & Classes" :opened="true">
   <a href="/w12/A#A"><span>Introducing OOP</span></a>
   <a href="/w12/A#B"><span>What are Objects</span></a>
   <a href="/w12/A#C"><span>State and Behavior</span></a>
   <a href="/w12/A#D"><span>What are Classes</span></a>
   <a href="/w12/A#E"><span>What is Encapsulation</span></a>
   <a href="/w12/A#F"><span>Real World Encapsulation</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="B-Encapsulation" :opened="true">
   <a href="/w12/B#A"><span>The Wall of Abstraction</span></a>
   <a href="/w12/B#B"><span>Class Definition Syntax</span></a>
   <a href="/w12/B#C"><span>Public and Private</span></a>
   <a href="/w12/B#D"><span>The Implicit Parameter</span></a>
   <a href="/w12/B#E"><span>The Pointer this</span></a>
   <a href="/w12/B#F"><span>The sum Member Function</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="C-Mutators & Constructors" :opened="true">
   <a href="/w12/C#A"><span>Setters</span></a>
   <a href="/w12/C#B"><span>Getter & Setter Patterns</span></a>
   <a href="/w12/C#C"><span>Constructors</span></a>
   <a href="/w12/C#D"><span>Member Initialization</span></a>
   <a href="/w12/C#E"><span>Working Constructor</span></a>
   <a href="/w12/C#F"><span>Assignment vs. Initialization</span></a>
   <a href="/w12/C#G"><span>The Initializer List</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="D-More on Classes" :opened="true">
   <a href="/w12/D#A"><span>The Working Constructor</span></a>
   <a href="/w12/D#B"><span>Conversion Constructors</span></a>
   <a href="/w12/D#C"><span>Implicit vs. Explicit</span></a>
   <a href="/w12/D#D"><span>Assign, Copy & Destroy</span></a>
   <a href="/w12/D#E"><span>Static Data Members</span></a>
   <a href="/w12/D#F"><span>Static Member Functions</span></a>
   <a href="/w12/D#G"><span>static const Data Members</span></a>
  </SidebarChapterHeading>
  <SidebarChapterHeading heading="E-Inheritance" :opened="true">
   <a href="/w12/E#A"><span>Classification</span></a>
   <a href="/w12/E#B"><span>Inheritance</span></a>
   <a href="/w12/E#C"><span>Person &lt;- Student</span></a>
   <a href="/w12/E#D"><span>The UML Diagram</span></a>
   <a href="/w12/E#E"><span>Inherited Members</span></a>
   <a href="/w12/E#F"><span>Private Base-class Members</span></a>
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
