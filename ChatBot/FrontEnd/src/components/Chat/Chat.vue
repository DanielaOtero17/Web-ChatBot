<script setup>

import {ref} from 'vue'


const text = ref('')
  const messages = ref([])

  function onClick () {
    messages.value.push(text.value)
  }


</script>

<template>


    <v-container class="chatcontainer ">
        <v-container class="chatHead ">
            <v-avatar image="src\assets\avatarBot.avif" size="60" />
            <h1 class="chatTitle">Mini ChatBot</h1>
        </v-container>
        
    <v-container class="chatEnd">
        <v-text-field placeholder="Haz una pregunta ..." variant="regular" class="entryMessage">
            
        </v-text-field>
        <v-btn elevation="0" color="#FAFAFA" height="60" append-icon="mdi-send"></v-btn>

    </v-container>
        
            
    </v-container>



</template>

<style scoped>


.chatcontainer{
    background-color: hsl(0, 0%, 96%);
    border-radius: 10px;
    padding: 0px;
    width: 800px;
    height: 500px;
}

.chatHead{

    background-color: rgb(16, 135, 214);
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
    margin-top: 355px;
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

v-btn{
    align-self: flex-end;
}

</style>




