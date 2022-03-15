<template lang="html">
  <div>
    <p>{{ $t('version') }} {{ packageVersion }}</p>
    <hr />
    <Spinner v-if="isLoading"></Spinner>
    <router-view />
  </div>
</template>

<script>
import verifyToken from '@/graphql/mutations/verifyToken.gql';
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
  },
  mounted() {
    // this.$apollo
    //   .mutate({ mutation: verifyToken })
    //   .then(() => {
    //     this.$store.state.isAuthenticated = true;
    //   })
    //   .catch((error) => {
    //     if (this.$route.path != '/auth') {
    //       this.$router.push('/auth');
    //     }
    //   })
    //   .finally(() => {
    //     this.$store.state.gotVerifiedAuth = true;
    //   });
  },
};
</script>
