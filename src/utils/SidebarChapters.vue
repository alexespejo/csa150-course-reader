<script setup>
const props = defineProps(["heading", "opened"]);
</script>

<template>
 <div class="collapse collapse-arrow bg-slate-300 dark:bg-slate-700">
  <input type="checkbox" :checked="opened" />
  <div class="collapse-title text-sm md:text-base font-bold">
   {{ props.heading }}
  </div>
  <div class="collapse-content">
   <slot />
  </div>
 </div>
</template>
