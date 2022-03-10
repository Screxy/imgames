import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

const store = new Vuex.Store({
  strict: true,
  state: {
    isAuthenticated: false,
    isLoading: false,
    gotVerifiedAuth: false,
  },
  mutations: {
    START_LOADING(state) {
      state.isLoading = true;
    },
    STOP_LOADING(state) {
      state.isLoading = false;
    },
    SET_IS_AUTHENTICATED(state, boolean) {
      state.isAuthenticated = boolean;
    },
    SET_GOT_VERIFIED_AUTH(state, boolean) {
      state.gotVerifiedAuth = boolean;
    },
  },
  actions: {},
});

export default store;
