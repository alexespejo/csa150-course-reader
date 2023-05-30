<script setup>
const props = defineProps(["prev", "next"]);
</script>
<template>
 <div
  class="flex border-4 bg-blue-500 text-blue-100 border-slate-800 min-w-fit w-fit rounded-lg self-end"
 >
  <a
   v-if="prev"
   :href="prev"
   :class="prev && next ? 'border-r-2 border-black' : ''"
   >Previous</a
  >
  <a v-if="next" :href="next">Next</a>
 </div>
</template>

<style scoped>
a {
 @apply py-2 px-4 font-bold hover:bg-blue-400 cursor-pointer;
}
</style>
