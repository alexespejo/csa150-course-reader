<script setup lang="ts">
import { ref } from "vue";
let letters = ref(["A", "B", "C", "D", "E", "F", "G", "H"]);
const props = defineProps(["sections"]);
</script>
<template>
 <div class="dropdown dropdown-bottom dropdown-end xl:hidden">
  <label
   tabindex="0"
   class="btn bg-orange-400 text-white m-1 hover:border-orange-400"
   >Index</label
  >
  <ul
   tabindex="0"
   class="dropdown-content menu shadow bg-slate-300 dark:bg-base-100 rounded-box w-72"
  >
   <a
    v-for="(sec, index) in props.sections"
    :key="index"
    :href="`#${letters[index]}`"
    class="p-0.5 dark:hover:underline py-3"
   >
    <li>{{ sec }}</li>
   </a>
  </ul>
 </div>
</template>
