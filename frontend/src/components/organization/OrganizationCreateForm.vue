<template>
  <form @submit.prevent ref="organizationCreateForm">
    <TextInput
      :placeholder="'Название'"
      :disabled="formLoading"
      @input="
        newOrganization != undefined ? (newOrganization.name = $event) : ''
      "
    ></TextInput>
    <TextInput
      :placeholder="'Поддомен'"
      :disabled="formLoading"
      @input="newOrganization.subdomain = $event"
    ></TextInput>
    <TextInput
      :placeholder="'Префикс'"
      :disabled="formLoading"
      @input="newOrganization.prefix = $event"
    ></TextInput>
    <SubmitButton :disabled="formLoading" @click="createNewOrganization">
      {{ $t('buttons.create') }}
    </SubmitButton>
  </form>
</template>

<script>
import TextInput from '@/components/ui/TextInput.vue';
import SubmitButton from '@/components/ui/SubmitButton.vue';
import createOrganization from '@/graphql/mutations/organizations/createOrganization.gql';

export default {
  name: 'OrganizationCreateForm',
  components: {
    TextInput,
    SubmitButton,
  },
  data() {
    return {
      newOrganization: {
        name: '',
        subdomain: '',
        prefix: '',
      },
      formLoading: false,
    };
  },
  methods: {
    async createNewOrganization() {
      this.$store.commit('START_LOADING');
      this.formLoading = true;
      console.log('newOrganization', this.newOrganization);
      this.$apollo
        .mutate({
          mutation: createOrganization,
          variables: this.newOrganization,
        })
        .then((data) => {
          console.log('data', data);
          let test_element = document.createElement('p');
          test_element.innerHTML = '' + JSON.stringify(data);
          this.$refs.organizationCreateForm.appendChild(test_element);
        })
        .catch((error) => {
          console.error(error);
        })
        .finally(() => {
          this.formLoading = false;
          this.$store.commit('STOP_LOADING');
        });
    },
  },
};
</script>

<style lang="scss" scoped></style>
