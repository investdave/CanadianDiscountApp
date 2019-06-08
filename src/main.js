import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

new Vue({
  render: h => h(App),
}).$mount('#app')
