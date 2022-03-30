<template>
  <div>
    <SubmitButton @click="sendCardChoice" :disabled="isDisabled">{{
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
  computed: {
    roomCode() {
      return this.$route.params.roomCode;
    },
    isDisabled() {
      return this.disabled || this.isLoading;
    },
  },
  methods: {
    sendCardChoice() {
      console.log('Отправляем массив: ', this.selectedCardsId);
      this.isLoading = true;
      // TODO: add mutation support
      this.$apollo
        .mutate({
          mutation: writeTurn,
          variables: {
            code: this.roomCode,
            cardsId: this.selectedCardsId,
          },
          update: (store, { data: { writeTurn } }) => {
            console.log('DATA FOR CACHE', writeTurn);
          },
        })
        .then(() => {})
        .catch((e) => {
          console.log(e);
          //
          // EMIT CLEAN CHOICE
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
  },
};
</script>

<style lang="scss" scoped></style>
