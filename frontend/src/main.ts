import { createApp, provide, h } from 'vue'
import { DefaultApolloClient } from '@vue/apollo-composable'
import { createPinia } from 'pinia'
import { apolloClient } from '@/apollo'
import App from '@/App.vue'
import router from '@/router/router'
import Pusher from 'pusher-js'
import FlagIcon from 'vue-flag-icon'
import * as Sentry from '@sentry/vue'
import './plugins/registerServiceWorker'
import i18n from '@/plugins/i18n'

// window.pusher = new Pusher(process.env.VUE_APP_PUSHER_KEY as string, {
//   cluster: process.env.VUE_APP_PUSHER_CLUSTER as string,
// });

// const DEFAULT_TITLE = 'ImGames';
// router.afterEach((to: any, from: any) => {
//   Vue.nextTick(() => {
//     document.title = to.meta.title || DEFAULT_TITLE;
//   });
// });
// TODO:
// import VueYandexMetrika from 'vue-yandex-metrika';
// app.use(VueYandexMetrika, {
//   id: process.env.VUE_APP_YANDEX_METRIKA,
//   env: process.env.NODE_ENV,
//   router,
// });
const app = createApp({
  setup() {
    provide(DefaultApolloClient, apolloClient)
  },

  render: () => h(App),
})
// Sentry для логирования ошибок фронтенда
// Sentry.init({
//   app,
//   dsn: process.env.VUE_APP_SENTRY_PUBLIC_DSN,
//   integrations: [
//     new Sentry.BrowserTracing({
//       routingInstrumentation: Sentry.vueRouterInstrumentation(router),
//     }),
//     new Sentry.Replay(),
//   ],
//   tracingOptions: {
//     trackComponents: true,
//   },
//   // Set tracesSampleRate to 1.0 to capture 100%
//   // of transactions for performance monitoring.
//   // We recommend adjusting this value in production
//   tracesSampleRate: 1.0,

//   // Set `tracePropagationTargets` to control for which URLs distributed tracing should be enabled
//   tracePropagationTargets: ['localhost', /^https:\/\/yourserver\.io\/api/],

//   // Capture Replay for 10% of all sessions,
//   // plus for 100% of sessions with an error
//   replaysSessionSampleRate: 0.1,
//   replaysOnErrorSampleRate: 1.0,
// });
const pinia = createPinia()
app.use(pinia)
app.use(i18n)

app.use(FlagIcon)
app.use(router)
app.mount('#app')
