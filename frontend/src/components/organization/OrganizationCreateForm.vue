<template>
  <form @submit.prevent>
    <TextInput
      :placeholder="'Название'"
      @input="newOrganization.name = $event"
    ></TextInput>
    <TextInput
      :placeholder="'Поддомен'"
      @input="newOrganization.subdomain = $event"
    ></TextInput>
    <TextInput
      :placeholder="'Префикс'"
      @input="newOrganization.prefix = $event"
    ></TextInput>
    <SubmitButton @click=""></SubmitButton>
  </form>
</template>

<script>
import TextInput from '@/components/ui/TextInput.vue';
import SubmitButton from '@/components/ui/SubmitButton.vue';

export default {
  name: 'OrganizationCreateForm',
  components: {
    TextInput,
    SubmitButton,
  },
  data: {
    newOrganization: {
      name: '',
      subdomain: '',
      prefix: '',
    },
  },
};
</script>

<style lang="scss" scoped></style>
