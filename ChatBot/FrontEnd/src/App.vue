<script setup>
import LeftBubble from './components/Bubble/LeftBubble.vue'

const messageTest = "Este es un mensaje inicial de prueba. Lalala"

</script>

<template>
  <header>
  
  </header>

  <main>
  <LeftBubble :message="messageTest" />
  </main>
</template>

<style scoped>

@media (min-width: 1024px) {
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
}

</style>
