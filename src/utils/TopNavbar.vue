<script setup>
import DropDownNavigation from "./DropDownNavigation.vue";
import ChapterSidebar from "./ChapterSideBar.vue";
import { ref } from "vue";
const showNavbar = ref(false);
const changeShowNavbar = () => {
 //  alert("printer");
 showNavbar.value = !showNavbar.value;
};
const props = defineProps(["sections"]);
</script>

<template>
 <div
  class="z-50 w-screen h-screen absolute top-0 lg:hidden bg-slate-700/50"
  v-if="showNavbar"
 >
  <div
   class="w-full h-full md:w-1/2 overflow-auto bg-slate-200 dark:bg-slate-900"
  >
   <div class="flex flex-row-reverse pr-5 py-2">
    <button
     class="btn text-white bg-blue-400 hover:bg-blue-400"
     @click="changeShowNavbar"
    >
     Close
    </button>
   </div>
   <ChapterSidebar />
  </div>
 </div>
 <nav id="navbar" class="h-full flex items-center px-3">
  <button
   class="flex flex-col space-y-1 lg:hidden"
   id="hamburger_menue"
   @click="changeShowNavbar"
  >
   <div class="bg-black dark:bg-white w-10 h-1 rounded-xl"></div>
   <div class="bg-black dark:bg-white w-10 h-1 rounded-xl"></div>
  </button>

  <div class="flex items-center ml-auto">
   <DropDownNavigation :sections="props.sections" />
   <h1 class="text-3xl font-bold ml-3">
    <span class="text-blue-700 dark:text-orange-400">CSA</span>150
   </h1>
  </div>
 </nav>
</template>
