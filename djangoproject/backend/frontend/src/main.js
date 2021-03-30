import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';
import router from './router'
import './plugins/element.js'

Vue.use(ElementUI)
Vue.config.productionTip = false

new Vue({
  router,
  components: { App },
  render: h => h(App),
  
}).$mount('#app')
