<template>
  <div>
    <!-- <TextInput
      :placeholder="$t('organization.prefix')"
      :disabled="formLoading"
      @input="newOrganization.prefix = $event"
    ></TextInput> -->
    <SubmitButton :disabled="formLoading" @click="createNewRoom">
      {{ $t('buttons.create') }}
    </SubmitButton>
  </div>
</template>

<script>
// import TextInput from '@/components/ui/TextInput.vue';
import SubmitButton from '@/components/ui/SubmitButton.vue';

export default {
  name: 'CreateRoomForm',
  components: {
    SubmitButton,
  },
  data() {
    return {
      formLoading: false,
    };
  },
  methods: {
    createNewRoom() {
      console.log('CreateRoomForm.vue');
    },
  },
};
</script>

<style lang="scss" scoped></style>
