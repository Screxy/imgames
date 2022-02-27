<template lang="html">
  <div>
    <Spinner v-if="isLoading"></Spinner>
    <router-view />
  </div>
</template>

<script>
import verifyToken from '@/graphql/mutations/verifyToken.gql';
import Spinner from '@/components/ui/Spinner.vue';

export default {
  name: 'App',
  components: { Spinner },
  computed: {
    isLoading() {
      return this.$store.state.isLoading;
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
