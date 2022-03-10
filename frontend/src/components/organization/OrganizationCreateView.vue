<template>
  <div>
    <h1>Создание организации</h1>
    <OrganizationCreateForm></OrganizationCreateForm>
  </div>
</template>

<script>
import OrganizationCreateForm from '@/components/organization/OrganizationCreateForm.vue';

export default {
  name: 'OrganizationCreateView',
  components: {
    OrganizationCreateForm,
  },
};
</script>

<style lang="scss" scoped></style>
