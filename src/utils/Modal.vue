<script setup>
import IconSearch from "../icons/IconSearch.vue";
import IconClose from "../icons/IconClose.vue";
import { onMounted } from "vue";

onMounted(() => {
 const showButton = document.getElementById("showDialog");
 const favDialog = document.getElementById("favDialog");
 const selectEl = favDialog.querySelector("select");
 const confirmBtn = favDialog.querySelector("#confirmBtn");

 // "Show the dialog" button opens the <dialog> modally
 showButton.addEventListener("click", () => {
  favDialog.showModal();
 });

 // "Favorite animal" input sets the value of the submit button
 selectEl.addEventListener("change", (e) => {
  confirmBtn.value = selectEl.value;
 });

 // "Cancel" button closes the dialog without submitting because of [formmethod="dialog"], triggering a close event.

 // Prevent the "confirm" button from the default behavior of submitting the form, and close the dialog with the `close()` method, which triggers the "close" event.
 confirmBtn.addEventListener("click", (event) => {
  event.preventDefault(); // We don't want to submit this fake form
  favDialog.close(selectEl.value); // Have to send the select box value here.
 });
});
</script>
<template>
 <!-- <label for="my_modal_6" class="btn space-x-2"
  ><span class="text-base">Search</span> <IconSearch
 /></label>

 <input type="checkbox" id="my_modal_6" class="modal-toggle" />
 <div class="modal ml-0 items-start">
  <div class="modal-box mt-5 h-1/2">
   <h3 class="font-bold text-lg">Hello!</h3>
   <p class="py-4">This modal works with a hidden checkbox!</p>
   <div class="modal-action">
    <label for="my_modal_6" class="btn">Close!</label>
   </div>
  </div>
 </div> -->
 <!-- A modal dialog containing a form -->
 <dialog
  id="favDialog"
  class="mt-5 w-full h-fit lg:w-1/2 rounded-xl bg-slate-200 dark:bg-slate-900 dark:text-slate-300 text-black text-sm md:text-base overflow-hidden py-3 border-2 border-slate-900 relative"
 >
  <form>
   <div class="flex-col flex">
    <button
     value="cancel"
     formmethod="dialog"
     class="dark:border-slate-900 dark:hover:border-slate-200 border-2 rounded-full self-end absolute top-1 right-2"
    >
     <IconClose />
    </button>
    <div class="">
     <slot />
    </div>
   </div>
  </form>
 </dialog>
 <button
  id="showDialog"
  class="btn bg-blue-700 dark:bg-orange-400 text-white hover:border-blue-400 dark:hover:border-orange-400"
 >
  <span class="mr-2 hidden lg:block">Search</span><IconSearch />
 </button>
 <output></output>
</template>

<style scoped>
dialog::backdrop {
 @apply bg-slate-500/80;
}
</style>
