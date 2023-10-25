<template>
  <div>
    <SubmitButton @click="logOut" :type="'light-text'">{{
      $t('buttons.logOut')
    }}</SubmitButton>
  </div>
</template>

<script setup lang="ts">
// import logout from '@/graphql/mutations/logout.gql';
// import { AUTH_PATH } from '@/pathVariables.js';
import SubmitButton from '@/components/ui/SubmitButton.vue';
import { useStore } from '@/stores/store';
const store = useStore()
function logOut() {
  store.isLoading = true
  // let logOutInterval = setInterval(() => {
  //   this.$apollo
  //     .mutate({ mutation: logout })
  //     .then(() => {
  //       clearInterval(logOutInterval);
  //       this.$store.commit('SET_IS_AUTHENTICATED', false);
  //       this.$router.push(AUTH_PATH);
  //       this.$store.commit('STOP_LOADING');
  //     })
  //     .catch(() => {})
  //     .finally(() => {});
  // }, 2000);
}
</script>

<style lang="scss" scoped></style>
