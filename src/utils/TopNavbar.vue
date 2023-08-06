<script setup>
import DropDownNavigation from "./DropDownNavigation.vue";
import ChapterSidebar from "./ChapterSideBar.vue";
import IconGithub from "../icons/IconGithub.vue";
import IconLegacyBook from "../icons/IconLegacyBook.vue";
import Modal from "../utils/Modal.vue";
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
  class="z-50 w-screen h-screen absolute top-0 lg:hidden flex"
  v-if="showNavbar"
 >
  <div
   class="w-full h-full md:w-1/2 overflow-auto bg-slate-200 dark:bg-slate-900"
  >
   <div class="flex p-2 items-center space-x-5">
    <button
     class="btn text-white bg-blue-400 hover:bg-blue-400"
     @click="changeShowNavbar"
    >
     &#8676; Close
    </button>

    <div class="tooltip tooltip-bottom" data-tip="View Original Book">
     <a
      class="dark:hover:text-white lg:hidden"
      href="https://www.occ-cs.com/book-23/"
     >
      <IconLegacyBook />
     </a>
    </div>
    <div class="tooltip tooltip-bottom lg:hidden" data-tip="Github">
     <a
      class="dark:hover:text-white"
      href="https://github.com/alexespejo/csa150-course-reader"
     >
      <IconGithub />
     </a>
    </div>
   </div>
   <ChapterSidebar />
  </div>
  <button
   class="hidden md:block w-1/2 h-screen bg-slate-700/50"
   @click="changeShowNavbar"
  ></button>
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
   <Modal client:load />
   <div
    class="tooltip tooltip-bottom mx-5 hidden lg:block"
    data-tip="View Original Book"
   >
    <a class="dark:hover:text-white" href="https://www.occ-cs.com/book-23/">
     <IconLegacyBook />
    </a>
   </div>
   <div class="tooltip tooltip-bottom hidden lg:block mr-5" data-tip="Github">
    <a
     class="dark:hover:text-white"
     href="https://github.com/alexespejo/csa150-course-reader"
    >
     <IconGithub />
    </a>
   </div>
   <DropDownNavigation :sections="props.sections" />
   <h1 class="text-3xl font-bold ml-3">
    <span class="text-blue-700 dark:text-orange-400">CSA</span>150
   </h1>
  </div>
 </nav>
</template>
