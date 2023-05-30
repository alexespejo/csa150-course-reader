<script setup>
const props = defineProps(["dir"]);
const list = ["A", "B", "C", "D", "E"];
</script>

<template>
 <div class="text-sm breadcrumbs items-center">
  <ul class="space-y-0">
   <li v-for="(i, index) in list" :key="index" class="list-none m-0">
    <a :href="`/${dir}/${i}`" class="">{{ i }}</a>
   </li>
  </ul>
 </div>
</template>

<style scoped>
ul {
 display: flex;
 flex-direction: row;
 align-items: center;
 margin: 0;
}
</style>
