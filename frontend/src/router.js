import Vue from 'vue';
import VueRouter from 'vue-router';
import { createProvider } from '@/apollo';

import ExampleComponent from '@/components/ExampleComponent.vue';
import AuthView from '@/components/auth/AuthView.vue';
import OrganizationCreateView from '@/components/organization/OrganizationCreateView.vue';

import store from '@/store.js';
import {
  MAIN_PATH,
  AUTH_PATH,
  NEW_ORGANIZATION_PATH,
} from '@/pathVariables.js';

import verifyToken from '@/graphql/mutations/verifyToken.gql';

function verifyAuth(to, from) {
  store.commit('START_LOADING');
  let provider = createProvider();
  return new Promise(function (resolve, reject) {
    provider.defaultClient
      .mutate({ mutation: verifyToken })
      .then(() => {
        store.commit('SET_IS_AUTHENTICATED', true);
      })
      .catch((error) => {
        store.commit('SET_IS_AUTHENTICATED', false);
      })
      .finally(() => {
        store.commit('SET_GOT_VERIFIED_AUTH', true);
        store.commit('STOP_LOADING');
        resolve();
      });
  });
}

const ifAuthenticated = async (to, from, next) => {
  try {
    if (!store.state.gotVerifiedAuth) {
      await verifyAuth(to, from);
    }
    if (store.state.isAuthenticated) {
      next();
      return;
    }
    next(AUTH_PATH);
  } catch (error) {
    console.log('ERROR TEST: ', error);
  }
};

const ifNotAuthenticated = async (to, from, next) => {
  try {
    if (!store.state.gotVerifiedAuth) {
      await verifyAuth(to, from);
    }
    if (!store.state.isAuthenticated) {
      next();
      return;
    }
    next(MAIN_PATH);
  } catch (error) {
    console.log('ERROR TEST: ', error);
  }
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
  {
    path: NEW_ORGANIZATION_PATH,
    component: OrganizationCreateView,
    beforeEnter: ifAuthenticated,
    meta: { title: 'Создать пространство - ImGames' },
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
