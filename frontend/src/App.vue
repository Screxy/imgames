<template lang="html">
  <div>
    <Spinner v-if="isLoading"></Spinner>
    <router-view />
  </div>
</template>

<script>
import Spinner from '@/components/ui/Spinner.vue';
import { version } from '../package.json';

export default {
  name: 'App',
  components: { Spinner },
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
  overflow-y: hidden;
  font-family: $primary_font;
}


h1, h2, h3, p {
  font-family: $primary_font;
  margin: 0;
  padding: 0.5rem 0;
  color: $dark_text_color;
}

.scrollable {
  overflow-y: auto;
  scrollbar-gutter: stable;
  &::-webkit-scrollbar {
    width: 16px;
  }
  &::-webkit-scrollbar-track {
    width: 16px;
    background-color: rgba(0,0,0,.1);
  }
  &::-webkit-scrollbar-thumb {
    backdrop-filter: blur(12px) saturate(100%);
    -webkit-backdrop-filter: blur(12px) saturate(100%);
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 12px;
    border: 1px solid rgba(209, 213, 219, 0.3);
  }
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

.default-background {
  background: radial-gradient(52.5% 97.01% at 21.67% 20.17%, rgba(82, 110, 255, 0.25) 0%, rgba(249, 216, 167, 0.25) 89.06%);
}

.error-message {
  color: $error;
}

.error-input {
  outline: 1px solid $error;
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
