<script setup lang="ts">
import { ref } from "vue";
let letters = ref(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]);
const props = defineProps(["sections"]);
</script>
<template>
 <div class="dropdown dropdown-bottom dropdown-end xl:hidden">
  <label
   tabindex="0"
   class="btn bg-blue-700 dark:bg-orange-400 text-white m-1 hover:border-blue-400 dark:hover:border-orange-400"
   >Index</label
  >
  <ul
   tabindex="0"
   class="dropdown-content menu shadow bg-slate-300 dark:bg-base-100 dark:border-2 dark:border-slate-200 w-56 sm:w-72"
  >
   <a
    v-for="(sec, index) in props.sections"
    :key="index"
    :href="`#${letters[index]}`"
    class="p-0.5 no-underline dark:hover:bg-slate-500 py-3 hover:dark:text-blue-300 hover:no-underline"
   >
    <li>{{ sec }}</li>
   </a>
  </ul>
 </div>
</template>
