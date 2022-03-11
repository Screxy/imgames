<template>
  <div>
    <h2>{{ $t('headers.organizationList') }}</h2>
    <div v-for="organization in organizationsByUser" :key="organization.id">
      <a :href="'http://' + organization.subdomain + '.' + getDomainName">
        Организация "{{ organization.name }}"
      </a>
      [{{ organization.prefix }}]
    </div>
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

<style lang="scss" scoped></style>
