<script setup>
const props = defineProps(["heading"]);
</script>

<template>
 <header class="text-sm p-1 font-bold border-b-2 border-slate-200 my-1">
  {{ props.heading }}
 </header>
 <div class="pl-4 text-sm"><slot /></div>
</template>

<style lang="scss">
a {
 @apply no-underline hover:underline;
 span {
  @apply block py-0.5 hover:bg-slate-600;
 }
}
</style>
