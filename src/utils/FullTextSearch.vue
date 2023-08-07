<script setup>
import { ref, computed } from "vue";
import chapters from "./chapters";

const list = chapters;

const query = ref("");

const computedList = computed(() => {
 const filteredList = list.filter((item) =>
  item.msg.toLowerCase().includes(query.value.toLowerCase())
 );
 console.log(filteredList);
 return filteredList;
});
</script>

<template>
 <div class="form-control w-full">
  <label class="label p-0 pb-1">
   <span class="label-text">Search for any topic</span>
  </label>
  <input
   v-model="query"
   placeholder="Type here"
   class="input input-bordered w-full"
  />
 </div>

 <ol class="h-80 overflow-auto space-y-0 space-x-0 mt-0.5 w-full">
  <li
   v-for="(item, index) in computedList"
   :key="item.msg"
   :data-index="index"
   class="list-none"
  >
   <a
    :href="item.href"
    class="no-underline hover:no-underline hover:text-blue-400 w-full"
   >
    <div
     class="text-base h-16 py-0.5 dark:hover:text-slate-300 dark:hover:bg-slate-400/50 relative p-1 flex items-center"
    >
     {{ item.msg }}
     <div class="absolute bottom-1 left-1 text-xs">
      Chapter {{ item.href.slice(2, 4) }}
     </div>
     <div class="text-xs absolute bottom-1 right-1">
      {{ item.heading }}
     </div>
    </div>
   </a>
  </li>
 </ol>
</template>

<style scoped>
li {
 @apply m-0 h-16;
}
</style>
