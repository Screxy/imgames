<template>
  <div>
    <h3>{{ $t('room.card.cardsList') }}</h3>
    <WriteTurnPanel
      :disabled="!canDoStepNowByCode"
      :selectedCardsId="selectedCardsId"
    ></WriteTurnPanel>
    <Card
      v-for="card in cardsByCode"
      :key="card.id"
      :data="card"
      :selected="isSelected(card.id)"
      :disabled="!canDoStepNowByCode"
      @select="addChoice($event)"
      @deselect="removeChoice($event)"
    ></Card>
  </div>
</template>

<script>
import cardsByCode from '@/graphql/queries/gameBoard/cardsByCode.gql';
import canDoStepNowByCode from '@/graphql/queries/gameBoard/canDoStepNowByCode.gql';
import Card from '@/components/room/playground/cardsList/Card.vue';
import WriteTurnPanel from '@/components/room/playground/cardsList/WriteTurnPanel.vue';

export default {
  name: 'CardsList',
  components: {
    Card,
    WriteTurnPanel,
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
    canDoStepNowByCode: {
      query: canDoStepNowByCode,
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
  },
};
</script>

<style lang="scss" scoped></style>
