import { defineStore } from "pinia";
import { ref } from "vue";

export const respuestaStore = defineStore('preguntar', () =>{
  const pregunta = ref('');

  const guardarPregunta = (mensajePregunta) => {
    pregunta.value = mensajePregunta;
  }

  return {pregunta, guardarPregunta}
});


