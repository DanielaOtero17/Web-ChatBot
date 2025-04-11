<script setup>

import {ref} from 'vue'
import LeftBubble from '../Bubble/LeftBubble.vue'

const messageText = {
    mensaje: "Hola soy DanielaBot. Estoy aquí para ayudarte",
    esRespuesta: true,    
}

const messagesList= ref([])

const textoModel = ref('');

messagesList.value.push(messageText)

const message2Text = {
    mensaje: "Este es otro mensaje de prueba",
    esRespuesta: false,    
}


const onClick = () =>{
    
    var msg = document.getElementById("textoPregunta").value;

    textoModel.value = "";

    const nuevoMensaje ={
        mensaje: msg,
        esRespuesta: false,
    }

    messagesList.value.push(nuevoMensaje)

  };

</script>

<template>

    <v-container class="chatcontainer ">
        <v-container class="chatHead ">
            <v-avatar image="src\assets\avatarBot.avif" size="60" />
            <h1 class="chatTitle">Mini ChatBot</h1>
        </v-container>


            <v-virtual-scroll
            :items="messagesList"
            height="450"
            item-height="48"
            >

            <template class="conversation" v-slot:default="{item}">
                <left-bubble :message=item.mensaje :es-respuesta=item.esRespuesta />
            </template>


            </v-virtual-scroll>
        

        <v-container class="chatEnd">
            <v-text-field id="textoPregunta" placeholder="Haz una pregunta ..." variant="regular" 
            class="entryMessage" 
            name="textoPregunta"
            v-model:model-value="textoModel"
            >
                
            </v-text-field>
            <v-btn elevation="0" color="#FAFAFA" height="60" append-icon="mdi-send" @Click="onClick"></v-btn>

        </v-container>
        
    </v-container>

</template>

<style scoped>


.chatcontainer{
    background-color: hsl(0, 0%, 96%);
    border-radius: 10px;
    padding: 0px;
    width: 700px;
    height: 600px;
}

.conversation{
    margin: 10px;
    padding: 10px;
}


.chatHead{

    background-color: rgb(16, 17, 17);
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;

    display: flex;
    align-items: center;
    justify-content: center;

}

.chatEnd{
    padding: 0px;
    display: flex;
    align-items: e;
}

.chatTitle{
    margin-left: 50px;
    color: white;
    border-color: rgb(32, 32, 32);
    text-shadow: black;
    text-overflow: clip;
}

.entryMessage{
    background-color: #FAFAFA;
    border-bottom-left-radius: 20px;

    height: 60px;
    
}

.v-btn{
    border-bottom-right-radius: 20px;
}



</style>




