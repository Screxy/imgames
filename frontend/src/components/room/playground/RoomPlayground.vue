<template>
  <div id="playground">
    <TopBar
      type="playground"
      :roomCode="roomCode"
      :roomRound="currentRoundKey"
      :roomMonth="currentMonthKey"
    ></TopBar>
    <div class="playField">
      <template v-if="!roomIsFinished">
        <WaitingScreen
          class="first-column-top"
          v-if="!roomIsActive"
          :roomCode="roomCode"
          @reloadRound="reloadRound()"
        ></WaitingScreen>
        <template v-else>
          <GameBoard class="first-column-top"></GameBoard>
          <CardsList class="first-column-bottom"></CardsList>
        </template>
        <PlayersList
          class="second-column-top"
          :players="players"
          :room="roomByCode"
          v-if="players != undefined && roomByCode != undefined"
        >
        </PlayersList>
        <EffectsList
          class="second-column-bottom"
          v-if="roomIsActive"
        ></EffectsList>
      </template>
      <template v-else>
        <FinishScreen
          :roundKey="currentRoundKey"
          :roomCode="roomCode"
          @reloadRound="reloadRound()"
        ></FinishScreen>
      </template>
      <div class="navigation">
        <div class="nav-btn">
          <img src="@/assets/icons/players.svg" alt="" />
          <p>{{ $t('room.navigation.players') }}</p>
        </div>
        <div class="nav-btn">
          <img src="@/assets/icons/star.svg" alt="" />
          <p>{{ $t('room.navigation.effects') }}</p>
        </div>
        <div class="nav-btn">
          <img src="@/assets/icons/chat.svg" alt="" />
          <p>{{ $t('room.navigation.chat') }}</p>
        </div>
        <div class="nav-btn">
          <img src="@/assets/icons/paper.svg" alt="" />
          <p>{{ $t('room.navigation.cards') }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import roomByCode from '@/graphql/queries/rooms/roomByCode.gql';
import currentRoundByCode from '@/graphql/queries/rooms/currentRoundByCode.gql';
import roomUpdated from '@/graphql/subscriptions/rooms/roomUpdated.gql';
import currentRoundUpdated from '@/graphql/subscriptions/rooms/currentRoundUpdated.gql';
import connectRoom from '@/graphql/mutations/rooms/connectRoom.gql';
import roomParticipants from '@/graphql/queries/rooms/roomParticipants.gql';
import roomParticipantsUpdated from '@/graphql/subscriptions/rooms/roomParticipantsUpdated.gql';
import PlayersList from '@/components/room/playground/PlayersList.vue';
import EffectsList from '@/components/room/playground/EffectsList.vue';
import GameBoard from '@/components/room/playground/gameBoard/GameBoard.vue';
import CardsList from '@/components/room/playground/cardsList/CardsList.vue';
import WaitingScreen from '@/components/room/playground/WaitingScreen.vue';
import FinishScreen from '@/components/room/playground/FinishScreen.vue';
import TopBar from '@/components/ui/TopBar.vue';
import { MAIN_PATH } from '@/pathVariables.js';

export default {
  name: 'RoomPlayground',
  components: {
    PlayersList,
    EffectsList,
    GameBoard,
    CardsList,
    WaitingScreen,
    FinishScreen,
    TopBar,
  },
  data() {
    return { skip: false };
  },
  computed: {
    roomCode() {
      return this.$route.params.roomCode;
    },
    currentRoundKey() {
      if (this.currentRoundByCode != undefined) {
        return this.currentRoundByCode.key;
      }
      return 0;
    },
    currentMonthKey() {
      if (this.currentRoundByCode != undefined) {
        if (this.currentRoundByCode.currentMonth != undefined) {
          return this.currentRoundByCode.currentMonth.key;
        }
      }
      return 0;
    },
    flow() {
      if (this.roomByCode != undefined) {
        if (this.roomByCode.flow != undefined) {
          return this.roomByCode.flow.title;
        }
      }
      return 0;
    },
    players() {
      if (this.roomByCode != undefined) {
        if (this.roomParticipants != undefined) {
          return this.roomParticipants;
        }
      }
      return [];
    },
    roomIsActive() {
      if (this.currentRoundByCode != undefined) {
        return this.currentRoundByCode.isActive;
      }
      return false;
    },
    roomIsFinished() {
      if (this.currentRoundByCode != undefined) {
        return this.currentRoundByCode.isFinished;
      }
      return false;
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
      subscribeToMore: {
        document: roomUpdated,
        variables() {
          return {
            code: this.roomCode,
          };
        },
        skip() {
          return this.skip;
        },
        updateQuery: (previousResult, { subscriptionData }) => {
          return { roomByCode: subscriptionData.data.roomUpdated };
        },
      },
    },
    currentRoundByCode: {
      query: currentRoundByCode,
      variables() {
        return {
          code: this.roomCode,
        };
      },
      subscribeToMore: {
        document: currentRoundUpdated,
        variables() {
          return {
            code: this.roomCode,
          };
        },
        skip() {
          return this.skip;
        },
        updateQuery: (previousResult, { subscriptionData }) => {
          return {
            currentRoundByCode: subscriptionData.data.currentRoundUpdated,
          };
        },
      },
    },
    roomParticipants: {
      query: roomParticipants,
      variables() {
        return {
          code: this.roomCode,
        };
      },
      subscribeToMore: {
        document: roomParticipantsUpdated,
        variables() {
          return {
            code: this.roomCode,
          };
        },
        skip() {
          return this.skip;
        },
        updateQuery: (previousResult, { subscriptionData }) => {
          let existIndex = previousResult.roomParticipants.findIndex(
            (el) => el.id == subscriptionData.data.roomParticipantsUpdated.id
          );
          if (existIndex == -1) {
            previousResult.roomParticipants.push(
              subscriptionData.data.roomParticipantsUpdated
            );
          }
          return {
            roomParticipants: previousResult.roomParticipants,
          };
        },
      },
    },
  },
  methods: {
    async reloadRound() {
      this.skip = true;
      await this.$apollo.queries.roomByCode.refresh();
      await this.$apollo.queries.currentRoundByCode.refresh();
      this.skip = false;
    },
  },
  mounted() {
    this.$apollo
      .mutate({
        mutation: connectRoom,
        variables: {
          code: this.roomCode,
        },
      })
      .then(() => {})
      .catch(() => {
        this.$router.push(MAIN_PATH);
      });
  },
};
</script>

<style lang="scss" scoped>
@import '@/scss/_variables.scss';

#playground {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: radial-gradient(
    52.5% 97.01% at 21.67% 20.17%,
    rgba(82, 110, 255, 0.25) 0%,
    rgba(249, 216, 167, 0.25) 89.06%
  );
  .playField {
    padding-left: 20px;
    display: grid;
    grid-template-columns: 2.8fr 1fr 62px;
    grid-template-rows: 1.6fr auto;
    height: 100%;
    column-gap: 20px;
    row-gap: 20px;

    & .first-column-top {
      grid-column-start: 1;
      grid-column-end: 2;
      grid-row-start: 1;
      grid-row-end: 2;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    & .first-column-bottom {
      grid-column-start: 1;
      grid-column-end: 2;
      grid-row-start: 2;
      grid-row-end: 3;
    }
    & .second-column-top {
      grid-column-start: 2;
      grid-column-end: 3;
      grid-row-start: 1;
      grid-row-end: 2;
    }
    & .second-column-bottom {
      grid-column-start: 2;
      grid-column-end: 3;
      grid-row-start: 2;
      grid-row-end: 3;
    }
    & .navigation {
      grid-column-start: 3;
      grid-column-end: 4;
      grid-row-start: 1;
      grid-row-end: 3;
    }
  }
}
.navigation {
  border-left: 1px solid $main_dark_bg_color;
  & .nav-btn {
    padding-top: 0.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    cursor: pointer;
    transition: 0.2s;
    & p {
      text-align: center;
      font-size: 12px;
    }
    & img {
      height: 48px;
    }
    &:hover {
      background-color: rgba(0, 0, 0, 0.1);
    }
  }
}
</style>
