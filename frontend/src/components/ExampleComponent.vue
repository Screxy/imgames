<template>
  <div class="container">
    <h1>{{ $t('headers.main') }}</h1>
    <LogOutButton></LogOutButton>
    Auth: {{ isAuthenticated }}<br />
    Host:{{ path }}<br />
    Locale:🌐 {{ $i18n.locale }} - {{ $t('message') }}<br />
    <LocaleSwitcher></LocaleSwitcher>
    <router-link to="/new">
      {{ $t('headers.organizationList') }}
    </router-link>
    <div>
      <OrganizationList></OrganizationList>
    </div>
    <hr />
    <div>
      <CreateRoomView></CreateRoomView>
    </div>
  </div>
</template>

<script>
import { AUTH_PATH } from '@/pathVariables.js';
import LogOutButton from '@/components/auth/LogOutButton.vue';
import LocaleSwitcher from '@/components/locale/LocaleSwitcher.vue';
import OrganizationList from '@/components/organization/OrganizationList.vue';
import CreateRoomView from '@/components/room/CreateRoomView.vue';

export default {
  name: 'FirstComponent',
  components: {
    LogOutButton,
    LocaleSwitcher,
    OrganizationList,
    CreateRoomView,
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
