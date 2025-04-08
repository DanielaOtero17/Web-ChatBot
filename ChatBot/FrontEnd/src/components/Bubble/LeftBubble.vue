<script setup>

const {messaje} = defineProps({
    message:{
        type: String,
        required: true,
    }
})
</script>

<template>

<div class="burbuja">{{message}}</div>

</template>

<style scoped>

.burbuja{
   /* width: fit-content;*/
    max-width: 300px;
    height: fit-content;
    
    padding: 5px;
    border-radius: 10px 10px 10px 0px;

    color: white;
    background-color: cornflowerblue;
}
</style>
