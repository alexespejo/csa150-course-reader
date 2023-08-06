<script setup>
import { ref, computed } from "vue";
import chapters from "./chapters";

const list = chapters;

const query = ref("");

const computedList = computed(() => {
 const filteredList = list.filter((item) =>
  item.msg.toLowerCase().includes(query.value)
 );
 console.log(filteredList);
 return filteredList;
});
</script>

<template>
 <input v-model="query" />
 <li v-for="(item, index) in computedList" :key="item.msg" :data-index="index">
  <a :href="item.href">
   <span class="text-sm"> {{ item.msg }}</span>
  </a>
 </li>
</template>
