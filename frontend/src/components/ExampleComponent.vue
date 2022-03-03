<template>
  <div class="container">
    <h1>Главная</h1>
    <LogOutButton></LogOutButton>
    Auth: {{ isAuthenticated }}<br />
    Host:{{ path }}<br />
    Locale:🌐 {{ $i18n.locale }} - {{ $t('message') }}<br />
    <LocaleSwitcher></LocaleSwitcher>
    Проверка изменений 2
  </div>
</template>

<script>
import { AUTH_PATH } from '@/pathVariables.js';
import LogOutButton from '@/components/auth/LogOutButton.vue';
import LocaleSwitcher from '@/components/locale/LocaleSwitcher.vue';

export default {
  name: 'FirstComponent',
  components: {
    LogOutButton,
    LocaleSwitcher,
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
    path() {
      return window.location.host;
    },
  },
};
</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
</style>
