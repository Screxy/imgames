<template>
  <div class="container">
    <h1>ImGames 2.0 - платформа для геймификации</h1>
    <router-link :to="authPath">AUTH</router-link>
    {{ isAuthenticated }}
  </div>
</template>

<script>
import { AUTH_PATH } from '@/pathVariables.js';

export default {
  name: 'FirstComponent',
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
