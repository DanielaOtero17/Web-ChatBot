import './assets/main.css'

import { createApp } from 'vue'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import "@mdi/font/css/materialdesignicons.css"

import App from './App.vue'


const vuetify = createVuetify({
    components,
    directives,
    icons: {
      defaultSet: "mdi",
    },
  })

/*export default createVuetify({
  icons: {
    defaultSet: 'mdi',
    aliases: {
      ...aliases,
      account: mdiAccount,
    },
    sets: {
      mdi,
    },
  },
})*/

createApp(App).use(vuetify).mount('#app')
