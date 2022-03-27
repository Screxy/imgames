<template>
  <div>
    <h3>{{ $t('room.card.cardsList') }}</h3>
    <SubmitButton @click="sendCardChoice">{{
      $t('room.card.send')
    }}</SubmitButton>
    <Card
      v-for="card in cardsByCode"
      :key="card.id"
      :data="card"
      :selected="isSelected(card.id)"
      @select="addChoice($event)"
      @deselect="removeChoice($event)"
    ></Card>
  </div>
</template>

<script>
import cardsByCode from '@/graphql/queries/gameBoard/cardsByCode.gql';
import Card from '@/components/room/playground/cardsList/Card.vue';
import SubmitButton from '@/components/ui/SubmitButton.vue';

export default {
  name: 'CardsList',
  components: {
    Card,
    SubmitButton,
  },
  apollo: {
    cardsByCode: {
      query: cardsByCode,
      variables() {
        return {
          code: this.roomCode,
        };
      },
    },
  },
  data() {
    return {
      selectedCardsId: [],
    };
  },
  computed: {
    roomCode() {
      return this.$route.params.roomCode;
    },
  },
  methods: {
    addChoice(cardId) {
      if (!this.isSelected(cardId)) {
        this.selectedCardsId.push(+cardId);
      }
    },
    removeChoice(cardId) {
      if (this.isSelected(cardId)) {
        this.selectedCardsId = this.selectedCardsId.filter(
          (el) => +el !== +cardId
        );
      }
    },
    isSelected(cardId) {
      return +this.selectedCardsId.findIndex((el) => +el == +cardId) !== -1;
    },
    sendCardChoice() {
      console.log('Отправляем массив: ', this.selectedCardsId);
    },
  },
};
</script>

<style lang="scss" scoped></style>
