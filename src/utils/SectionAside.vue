<script setup>
import { ref } from "vue";
let letters = ref(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]);
const props = defineProps(["sections"]);
</script>
<template>
 <div class="px-3 pt-2">
  <h1 class="hidden lg:block border-b-2 border-slate-200 text-lg font-bold">
   Index
  </h1>
  <ul class="">
   <a
    class="no-underline"
    v-for="(sec, index) in props.sections"
    :key="index"
    :href="`#${letters[index]}`"
   >
    <li>{{ sec }}</li>
   </a>
  </ul>
 </div>
</template>

<style lang="scss" scoped>
ul {
 @apply leading-none space-y-0;
 li {
  @apply list-none m-0 text-base  p-3 py-3  hover:underline  hover:text-blue-500 hover:dark:text-blue-300 w-full;
 }

 @media (min-width: 640px) {
  /* styles for screens with a minimum width of 640px */
 }

 @media (min-width: 768px) {
  /* styles for screens with a minimum width of 768px */
 }
}
</style>
