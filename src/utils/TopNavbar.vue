<script setup>
import DropDownNavigation from "./DropDownNavigation.vue";

const props = defineProps(["sections"]);
</script>
<template>
 <nav
  id="navbar"
  class="border-b-2 border-slate-300/60 h-full flex items-center px-3 flex-row-reverse"
 >
  <h1 class="text-3xl font-bold ml-3">
   <span class="text-blue-700 dark:text-orange-400">CSA</span>150
  </h1>
  <DropDownNavigation :sections="props.sections" />
 </nav>
</template>
