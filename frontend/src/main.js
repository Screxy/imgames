import Vue from 'vue';
import store from '@/store';
import router from '@/router';

import { createProvider } from '@/apollo';

import VueYandexMetrika from 'vue-yandex-metrika';

import * as Sentry from '@sentry/vue';
import { Integrations } from '@sentry/tracing';

import App from '@/App.vue';
import './registerServiceWorker';

Vue.config.productionTip = false;

// Sentry для логирования ошибок фронтенда
Sentry.init({
  Vue: Vue,
  dsn: process.env.VUE_APP_SENTRY_PUBLIC_DSN,
  integrations: [new Integrations.BrowserTracing()],
  tracingOptions: {
    trackComponents: true,
  },
  logError: process.env.NODE_ENV === 'development',
});

// Документация: https://github.com/vchaptsev/vue-yandex-metrika
Vue.use(VueYandexMetrika, {
  id: process.env.VUE_APP_YANDEX_METRIKA,
  env: process.env.NODE_ENV,
  router,
});

new Vue({
  router,
  store,
  provide: createProvider().provide(),
  render: (h) => h(App),
}).$mount('#app');
