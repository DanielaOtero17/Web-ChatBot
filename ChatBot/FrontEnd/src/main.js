import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import "@mdi/font/css/materialdesignicons.css"

import firebase from "firebase/compat/app";
// Required for side-effects
import "firebase/compat/firestore";

//Axios
import axiosInstance from './axios'

import App from './App.vue'


const vuetify = createVuetify({
    components,
    directives,
    icons: {
      defaultSet: "mdi",
    },
  })

const pinia = createPinia()

const firebaseConfig = {
  apiKey: "AIzaSyCPoEA5k64o5qCNJtQ6_HsnaCo6i33BHeg",
  authDomain: "minichatbot-92745.firebaseapp.com",
  projectId: "minichatbot-92745",
  storageBucket: "minichatbot-92745.firebasestorage.app",
  messagingSenderId: "861013643101",
  appId: "1:861013643101:web:7dd37abb9bd75aaab722b4",
  measurementId: "G-Z6KQBCLRTX"
};

firebase.initializeApp(firebaseConfig)

const app = createApp(App);

export const db = firebase.firestore();

app.use(vuetify)
app.use(pinia)
app.config.globalProperties.$axios = axiosInstance;
app.mount('#app')




