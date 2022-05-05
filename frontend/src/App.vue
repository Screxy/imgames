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
  overflow-x: hidden;
}

h2, h3, p {
  font-family: $primary_font;
  margin: 0;
  padding: 0.5rem 0;
  color: $dark_text_color;
}

.normal-border-box {
  // border: 2px solid;
  border-image-slice: 1 !important;
  border-image-source: linear-gradient(
    288.78deg,
    #4d3658 0%,
    #cddfe9 43.75%,
    #1da1ac 100%
  );
  // box-shadow: 2px 16px 19px 0px rgba(0, 0, 0, 0.09);
  // background: url(./assets/tile.png),
  //   radial-gradient(
  //     90.16% 143.01% at 15.32% 21.04%,
  //     rgba(224, 249, 255, 0.2) 0%,
  //     rgba(110, 191, 244, 0.0447917) 77.08%,
  //     rgba(70, 144, 213, 0) 100%
  //   );
  // background-blend-mode: overlay, normal;
  // filter: drop-shadow(2px 16px 19px rgba(0, 0, 0, 0.09));
  // backdrop-filter: blur(80px);
  // border-radius: 8px;
    backdrop-filter: blur(12px) saturate(100%);
    -webkit-backdrop-filter: blur(12px) saturate(100%);
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 12px;
    border: 1px solid rgba(209, 213, 219, 0.3);
}

.w-100 {
  width: 100%;
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
