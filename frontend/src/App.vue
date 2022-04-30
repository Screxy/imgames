<template lang="html">
  <div>
    <Spinner v-if="isLoading"></Spinner>
    <router-view />
    <hr />
    <p>{{ $t('version') }} {{ packageVersion }}</p>
    Auth: {{ isAuthenticated }}<br />
    Host:{{ path }}<br />
    Subdomain:{{ subdomain }}<br />
    Locale:🌐 {{ $i18n.locale }} - {{ $t('message') }}<br />
    <LocaleSwitcher></LocaleSwitcher>
  </div>
</template>

<script>
import Spinner from '@/components/ui/Spinner.vue';
import LocaleSwitcher from '@/components/locale/LocaleSwitcher.vue';
import { version } from '../package.json';

export default {
  name: 'App',
  components: { Spinner, LocaleSwitcher },
  computed: {
    isLoading() {
      return this.$store.state.isLoading;
    },
    packageVersion() {
      return version;
    },
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    },
    path() {
      return window.location.host;
    },
    subdomain() {
      return this.$store.state.subdomain;
    },
  }
};
</script>

<style lang="scss">
@import '@/scss/_variables.scss';

body {
  padding: 0;
  margin: 0;
}

h2 {
  font-family: $primary_font;
  margin: 0;
  padding: 0.5rem 0;
}

@font-face {
  font-family: "PT Sans";
  src: local("PT Sans"), url(./assets/fonts/PTSans/PTSans-Regular.ttf) format("truetype");
}

@font-face {
  font-family: "PT Sans Bold";
  src: local("PT Sans Bold"), url(./assets/fonts/PTSans/PTSans-Bold.ttf) format("truetype");
}
</style>
  
</style>
