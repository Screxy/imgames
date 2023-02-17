<template>
  <div id="cards-panel">
    <div class="cards-context">
      <h3 class="cards-title">{{ $t('room.card.moneyLeft') + ": " + balance}} </h3>
      <h3 class="waiting-for-players" v-if="!canDoStepNowByCode || waitingForOthers">
        {{ $t('room.card.waitingForOthers') }}
      </h3>
    </div>
    <WriteTurnPanel
      class="write-turn-panel"
      :disabled="balance < 0 || (!canDoStepNowByCode || waitingForOthers)"
      :selectedCardsId="selectedCardsId"
      @cardsAreSend="waitingForOthers = true"
    ></WriteTurnPanel>
    <div class="cards-list scrollable" ref='cardsList' :class='{fullScreen : isFull}'>
      {{ counter }}
      <Card
        v-for="card in cardsByCode"
        :key="card.id"
        :data="card"
        :selected="isSelected(card.id)"
        :disabled="!canDoStepNowByCode || waitingForOthers"
        :balance="balance"
        @select="addChoice($event)"
        @deselect="removeChoice($event)"
      ></Card>
      <div class="slider-arrow" @click="slideRight()" v-if='isOverflown'>
        <img src="@/assets/arrow.svg" alt="" />
      </div>
    </div>
  </div>
</template>

<script>
import cardsByCode from '@/graphql/queries/gameBoard/cardsByCode.gql';
import canDoStepNowByCode from '@/graphql/queries/gameBoard/canDoStepNowByCode.gql';
import roomByCode from '@/graphql/queries/rooms/roomByCode.gql';
import getMoneyPerMonth from '@/graphql/queries/gameBoard/getMoneyPerMonth.gql';
import Card from '@/components/room/playground/cardsList/Card.vue';
import WriteTurnPanel from '@/components/room/playground/cardsList/WriteTurnPanel.vue';

export default {
  name: 'CardsList',
  components: {
    Card,
    WriteTurnPanel,
  },
  props: {
    isFull: {
      type: Boolean,
    },
  },
  apollo: {
    roomByCode: {
      query: roomByCode,
      variables() {
        return {
          code: this.roomCode,
        };
      },
    },
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
    getMoneyPerMonth: {
      query: getMoneyPerMonth,
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
      balanceIsPositive: true,
      waitingForOthers: false,
      isOverflown: false,
      counter: 0,
    };
  },
  computed: {
    roomCode() {
      return this.$route.params.roomCode;
    },
    moneyPerMonth() {
      if (this.getMoneyPerMonth != undefined) {
        return this.getMoneyPerMonth;
      }
      return 0;
    },
    balance() {
      var expenses = 0;
      this.selectedCardsId.forEach(id => {
        this.cardsByCode.forEach(card => {
          if(card.id == id) {
            expenses = expenses + card.cost;
          };
        });
      });
      return this.moneyPerMonth - expenses;
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
          (el) => {
            return el != cardId;
          }
        );
      }
    },
    isSelected(cardId) {
      return +this.selectedCardsId.findIndex((el) => +el == +cardId) !== -1;
    },
    checkOverFlow() {
      let list = this.$refs.cardsList;
      if (list != undefined) {
        this.isOverflown = list.scrollWidth > list.offsetWidth
      }
      else {
        this.isOverflown = false
      }
      list.style.width = this.$el.offsetWidth + "px";
      this.counter+=1;
    },
  },
  mounted() {
    this.$root.$on('awaitIsOver', () => {
      this.waitingForOthers = false;
      this.$apollo.queries.canDoStepNowByCode.refresh();
      this.$apollo.queries.getMoneyPerMonth.refresh();
      this.selectedCardsId = [];
      this.$emit('clean');
    });
    this.$refs.cardsList.addEventListener("wheel", (e) => {
      e.preventDefault();
      this.$refs.cardsList.scrollLeft += (e.deltaY/1.5);
      this.checkOverFlow();
    });
    this.checkOverFlow();
    window.onresize = this.checkOverFlow;
  }
};
</script>

<style lang="scss" scoped>
#cards-panel {
  position: relative;
  display: flex;
  flex-direction: column;
  min-height: 300px;

  & .cards-context {
    display: flex;
  }

  & .cards-title {
    width: 50%;
  }


  & .cards-list {
    padding-right: 18px;
    overflow-y: auto;
    overflow-x: auto;
    display: flex;
    padding-bottom: 0.5rem;
    max-width: 70vw;
    box-shadow: inset 0px 0px 20px grey;
    height: fit-content;
    padding: 5px;
    background-color: lightgray;
    border-radius: 5px;
  }
  & .fullScreen {
    max-width: 100%;
    // max-width: 100%;
  }

  & .write-turn-panel {
    margin: 0 0 0.5rem 0;
  }
  .waiting-title {
    font-family: "PT Sans", sans-serif;
    font-size: 1.17em;
  }
}
@media screen and (max-width: 1150px) {
  h3 {
    display: none;
  }
  #cards-panel {
    & .cards-list {
      max-width: 99vw;
    }
  }
  .write-turn-panel {
    margin-top: 0.5rem;
  }
}
.slider-arrow {
  position: absolute;
  transition: all 0.25s;
  border-radius: 32px;
  top: 15px;
  right: 10px;
  z-index: 2;
  width: 64px;
  height: 64px;
  img {
    width: 100%;
    transition: all 0.25s;
    border-radius: 32px;
  }
}
.slider-arrow:hover {
  height: 72px;
  width: 72px;
  top: 11px;
  right: 6px;
  img {
    border-radius: 36px;
    cursor: pointer;
    width: 72px;
  }
}
.slider-arrow:active {
  transition: all 0.1;
  height: 54px;
  width: 54px;
  top: 20px;
  right: 15px;
  img {
    border-radius: 27px;
    cursor: pointer;
    width: 54px;
  }
}

.waiting-for-players {
  width: 50%;
  text-align: right;
  animation-name: fadeIn;
  animation-duration: 0.75s;
  animation-iteration-count: infinite;

}
@keyframes fadeIn {  
	0% { opacity: 50%; }
  50% { opacity: 100%; }
	100% { opacity: 50%;}
}


</style>
