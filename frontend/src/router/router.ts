import { createRouter, createWebHistory } from 'vue-router';
// import { createProvider } from '@/apollo';

import Main from '@/components/Main.vue';
import AuthView from '@/components/auth/AuthView.vue';
// import OrganizationCreateView from '@/components/organization/OrganizationCreateView.vue';
// import RoomPlayground from '@/components/room/playground/RoomPlayground.vue';
// import SignUpView from '@/components/auth/SignUpView.vue';
// import SignUpConfirmView from '@/components/auth/SignUpCofirmView.vue';
// import EditProfile from '@/components/auth/EditProfile.vue';
// import ResetPasswordView from '@/components/auth/ResetPasswordView.vue';
// import setNewPasswordView from '@/components/auth/setNewPasswordView.vue';

import { useStore } from '@/stores/store';
import {
  MAIN_PATH,
  AUTH_PATH,
  NEW_ORGANIZATION_PATH,
  ROOMS_ROOT_PATH,
  SIGN_UP_PATH,
  SIGN_UP_CONFIRM_PATH,
  AUTH_EDIT_PROFILE_PATH,
  RESET_PASSWORD_PATH,
  SET_NEW_PASSWORD_PATH,
} from '@/router/pathVariables';

// import verifyToken from '@/graphql/mutations/verifyToken.gql';
// import profile from '@/graphql/queries/profile.gql';

export function verifyAuth(to: any, from: any) {
  const store = useStore();

  store.isLoading = true;
  store.isLoading = false;
  // let provider = createProvider();
  return new Promise<void>(function (resolve, reject) {
    // provider.defaultClient
    // .mutate({ mutation: verifyToken })
    // .then((result: any) => {
    //   let userId = result.data.verifyToken.payload.user_id;
    //   store.SET_USER_ID(userId);
    //   store.SET_IS_AUTHENTICATED(true);
    //   setProfile(provider, userId);
    // })
    // .catch((error: any) => {
    //   store.SET_IS_AUTHENTICATED(false);
    // })
    // .finally(() => {
    //   store.SET_GOT_VERIFIED_AUTH(true);
    //   store.STOP_LOADING();
    //   resolve();
    // });
  });
}

async function setProfile(provider: any, userId: any) {
  return new Promise(function (resolve, reject) {
    // provider.defaultClient.mutate({ mutation: profile }).then((result: any) => {
    // store.SET_USER_NAME(
    //   result.data.profile.firstName + ' ' + result.data.profile.lastName
    // );
    // store.SET_PERMISSIONS({
    //   isStaff: result.data.profile.isStaff,
    //   isAdmin: result.data.profile.isAdmin,
    // });
    // });
  });
}

const ifAuthenticated = async (to: any, from: any, next: any) => {
  const store = useStore();

  try {
    if (!store.gotVerifiedAuth) {
      await verifyAuth(to, from);
    }
    if (store.isAuthenticated) {
      next();
      return;
    }
    next(AUTH_PATH);
  } catch (error) {
    console.log('ERROR TEST: ', error);
  }
};

const ifNotAuthenticated = async (to: any, from: any, next: any) => {
  const store = useStore();

  try {
    if (!store.gotVerifiedAuth) {
      await verifyAuth(to, from);
    }
    if (!store.isAuthenticated) {
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
    component: Main,
    beforeEnter: ifAuthenticated,
    meta: { title: 'Главная - ImGames' },
  },
  {
    path: AUTH_PATH,
    component: AuthView,
    // beforeEnter: ifNotAuthenticated,
    meta: { title: 'Войти - ImGames' },
  },
  // {
  //   path: SIGN_UP_PATH,
  //   component: SignUpView,
  //   beforeEnter: ifNotAuthenticated,
  //   meta: { title: 'Зарегистрироваться - ImGames' },
  // },
  // {
  //   path: AUTH_EDIT_PROFILE_PATH,
  //   component: EditProfile,
  //   beforeEnter: ifAuthenticated,
  //   meta: { title: 'Редактировать профиль - ImGames' },
  // },
  // {
  //   path: NEW_ORGANIZATION_PATH,
  //   component: OrganizationCreateView,
  //   beforeEnter: ifAuthenticated,
  //   meta: { title: 'Создать пространство - ImGames' },
  // },
  // {
  //   path: ROOMS_ROOT_PATH + '/:roomCode',
  //   component: RoomPlayground,
  //   beforeEnter: ifAuthenticated,
  //   meta: { title: 'Игровая комната' },
  // },
  // {
  //   path: SIGN_UP_CONFIRM_PATH + '/:token',
  //   component: SignUpConfirmView,
  //   beforeEnter: ifNotAuthenticated,
  //   meta: { title: 'Подтверждение регистрации' },
  // },
  // {
  //   path: RESET_PASSWORD_PATH,
  //   component: ResetPasswordView,
  //   beforeEnter: ifNotAuthenticated,
  //   meta: { title: 'Восстановление пароля' },
  // },
  // {
  //   path: SET_NEW_PASSWORD_PATH,
  //   component: setNewPasswordView,
  //   beforeEnter: ifNotAuthenticated,
  //   meta: { title: 'Восстановление пароля' },
  // },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
