<template>
  <div>
    <h2>{{ $t('headers.organizationList') }}</h2>
    <SubmitButton
      class="new-organization-btn"
      :type="'bg-outline'"
      @click="$router.push('/new')"
      >{{ $t('headers.organizationList') }}</SubmitButton
    >
    <div
      class="normal-border-box organizations-list-item"
      v-for="organization in organizationsByUser"
      :key="organization.id"
    >
      {{ $t('organization.organization') }} "{{ organization.name }}"
      <a :href="'http://' + organization.subdomain + '.' + getDomainName">
        <br />
        {{ 'http://' + organization.subdomain + '.' + getDomainName }}
      </a>
    </div>
  </div>
</template>

<script>
import organizationsByUser from '@/graphql/queries/organizationsByUser.gql';
import SubmitButton from '@/components/ui/SubmitButton.vue';

export default {
  name: 'OrganizationList',
  components: {
    SubmitButton,
  },
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
@import '@/scss/_variables.scss';

h2 {
  text-align: center;
}
.organizations-list-item {
  padding: 1rem;
  font-family: $primary_font;
  color: $dark_text_color;
  font-size: 14px;
  margin-bottom: 0.5rem;
  margin-right: 0.5rem;
}

.new-organization-btn {
  margin-bottom: 1rem;
  width: calc(100% - 0.5rem);
}
</style>
