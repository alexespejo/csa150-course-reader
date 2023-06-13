<script setup>
import { ref } from "vue";
let letters = ref(["A", "B", "C", "D", "E", "F", "G", "H"]);
const props = defineProps(["sections"]);
</script>
<template>
 <ul class="py-5">
  <a
   class="no-underline"
   v-for="(sec, index) in props.sections"
   :key="index"
   :href="`#${letters[index]}`"
  >
   <li>{{ sec }}</li>
  </a>
 </ul>
</template>

<style lang="scss" scoped>
ul {
 @apply leading-none space-y-0;
 li {
  @apply list-none m-0 text-base p-3 py-3 xl:text-sm hover:underline hover:bg-slate-300 hover:dark:bg-slate-800 w-full;
 }

 @media (min-width: 640px) {
  /* styles for screens with a minimum width of 640px */
 }

 @media (min-width: 768px) {
  /* styles for screens with a minimum width of 768px */
 }
}
</style>
