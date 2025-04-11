<script setup>

const {message, esRespuesta} = defineProps({
    message:{
        type: String,
        required: true,
    },
    esRespuesta:{
        type:Boolean,
        required: true,
        default: false,
    }
})

</script>

<template>

<div v-if="esRespuesta" class="itemBot">
    <v-avatar image="src\assets\avatarBot.avif" size="40" />
    <div  class="burbujaBot" >
        {{message}} 
    </div>
</div>
<div v-else class="itemUser">
    
    <div  class="burbujaUser" >
        {{message}} 
    </div>
    <v-avatar image="src\assets\avatarUsuario.png" size="40" />
</div>


</template>

<style scoped>

.burbujaBot, .burbujaUser{
    width: fit-content;
    max-width: 500px;
    
    min-height: 30px;
    max-height: fit-content;
    
    padding: 10px;
    
    margin: 10px;
    margin-top: 20px;
}

.itemUser, .itemBot{
    display: flex;
    align-items:center;
}

.itemBot{
    margin-left: 10px;
}

.itemUser{
 justify-content: right;
 margin-right: 10px;
}

.burbujaBot{
    color: white;
    background-color: rgb(16, 135, 214);
    border-radius: 10px 10px 10px 0px;
}

.burbujaUser{
    color: rgb(10, 10, 10);
    background-color: white;
    border-radius: 10px 10px 0px 10px;
    right: 5px;
   /* position:absolute;*/
 
    
}
</style>
