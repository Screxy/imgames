import Vue from 'vue';
import VueRouter from 'vue-router';
import { createProvider } from '@/apollo';

import ExampleComponent from '@/components/ExampleComponent.vue';
import AuthView from '@/components/auth/AuthView.vue';

import store from '@/store.js';
import { MAIN_PATH, AUTH_PATH } from '@/pathVariables.js';

import verifyToken from '@/graphql/mutations/verifyToken.gql';

function verifyAuth() {
  store.commit('START_LOADING');
  let provider = createProvider();
  return new Promise(function (resolve, reject) {
    provider.defaultClient
      .mutate({ mutation: verifyToken })
      .then(() => {
        store.state.isAuthenticated = true;
      })
      .catch((error) => {
        if (this.$route.path != '/auth') {
          this.$router.push('/auth');
        }
      })
      .finally(() => {
        store.state.gotVerifiedAuth = true;
        store.commit('STOP_LOADING');
        resolve();
      });
  });
}

const ifAuthenticated = async (to, from, next) => {
  if (!store.state.gotVerifiedAuth) {
    await verifyAuth();
  }
  if (store.state.isAuthenticated) {
    next();
    return;
  }
  next(AUTH_PATH);
};

const ifNotAuthenticated = async (to, from, next) => {
  if (!store.state.gotVerifiedAuth) {
    await verifyAuth();
  }
  if (!store.state.isAuthenticated) {
    next();
    return;
  }
  next(MAIN_PATH);
};

const routes = [
  {
    path: '',
    component: ExampleComponent,
    beforeEnter: ifAuthenticated,
    meta: { title: 'Главная - ImGames' },
  },
  {
    path: AUTH_PATH,
    component: AuthView,
    beforeEnter: ifNotAuthenticated,
    meta: { title: 'Войти - ImGames' },
  },
];

Vue.use(VueRouter);
const router = new VueRouter({
  scrollBehavior(to, from, savedPosition) {
    return { x: 0, y: 0 };
  },
  mode: 'history',
  routes,
});

export default router;
