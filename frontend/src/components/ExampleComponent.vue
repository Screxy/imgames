<template>
  <div class="container">
    <h1>Главная</h1>
    <LogOutButton></LogOutButton>
    {{ isAuthenticated }}
  </div>
</template>

<script>
import { AUTH_PATH } from '@/pathVariables.js';
import LogOutButton from '@/components/auth/LogOutButton.vue';

export default {
  name: 'FirstComponent',
  components: {
    LogOutButton,
  },
  data() {
    return {
      authPath: AUTH_PATH,
    };
  },
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    },
  },
};
</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
</style>
