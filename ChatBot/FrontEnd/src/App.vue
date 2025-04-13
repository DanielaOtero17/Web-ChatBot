<script setup>

import Chat from './components/Chat/Chat.vue';

</script>

<template>

  <v-app>

  <Chat></Chat>

  </v-app>

</template>

<style scoped>


  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

</style>
