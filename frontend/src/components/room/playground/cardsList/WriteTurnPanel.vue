<template>
  <div>
    <SubmitButton @click="sendCardChoice" :disabled="isDisabled()">{{
      $t('room.card.send')
    }}</SubmitButton>
  </div>
</template>

<script>
import SubmitButton from '@/components/ui/SubmitButton.vue';
import writeTurn from '@/graphql/mutations/rooms/writeTurn.gql';

export default {
  name: 'WriteTurnPanel',
  props: {
    disabled: {
      type: Boolean,
      default: false,
    },
    selectedCardsId: {
      type: Array,
      default: [],
    },
  },
  components: {
    SubmitButton,
  },
  data() {
    return {
      isLoading: false,
    };
  },
  methods: {
    isDisabled() {
      return this.disabled || isLoading;
    },
    sendCardChoice() {
      console.log('Отправляем массив: ', this.selectedCardsId);
      // TODO: add mutation support
      // this.$apollo.mutate();
    },
  },
};
</script>

<style lang="scss" scoped></style>
