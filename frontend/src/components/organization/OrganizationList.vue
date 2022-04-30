<template>
  <div>
    <h2>{{ $t('headers.organizationList') }}</h2>
    <div v-for="organization in organizationsByUser" :key="organization.id">
      <a :href="'http://' + organization.subdomain + '.' + getDomainName">
        {{ $t('organization.organization') }} "{{ organization.name }}"
      </a>
      [{{ organization.prefix }}]
    </div>
    <router-link to="/new">
      {{ $t('headers.organizationList') }}
    </router-link>
  </div>
</template>

<script>
import organizationsByUser from '@/graphql/queries/organizationsByUser.gql';

export default {
  name: 'OrganizationList',
  data() {
    return {
      organizationsByUser: {},
    };
  },
  computed: {
    getDomainName() {
      let hostName = location.host;
      return hostName.substring(
        hostName.lastIndexOf('.', hostName.lastIndexOf('.') - 1) + 1
      );
    },
  },
  apollo: {
    organizationsByUser: {
      query: organizationsByUser,
    },
  },
};
</script>

<style lang="scss" scoped>
h2 {
  text-align: center;
  position: sticky;
  top: 0;
  left: 0;
}
</style>
