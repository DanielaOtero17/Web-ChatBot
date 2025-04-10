<script setup>

import Chat from './components/Chat/Chat.vue';


const messageTest = "Este es un mensaje inicial de prueba. Lalala"

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
