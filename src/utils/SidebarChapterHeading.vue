<script setup>
const props = defineProps(["heading"]);
</script>

<template>
 <div class="bg-slate-800 p-1">
  <header class="text-sm p-1 font-bold border-b-2 border-slate-200 my-1">
   {{ props.heading }}
  </header>
  <div class="text-sm"><slot /></div>
 </div>
</template>

<style lang="scss">
a {
 @apply no-underline hover:underline;
 span {
  @apply block py-0.5 pl-4 dark:hover:bg-slate-600;
 }
}
</style>
