<template>
  <div>
    <h1>{{ $t('room.room') }} {{ roomCode }}</h1>
    <template v-if="!roomIsFinished">
      <WaitingScreen
        v-if="!roomIsActive"
        :roomCode="roomCode"
        @reloadRound="reloadRound"
      ></WaitingScreen>
      <template v-else>
        <h2>
          {{ $t('room.mechanics') }} "{{ flow }}" / {{ $t('room.round') }} R{{
            currentRoundKey
          }}
          / {{ $t('room.month') }} M{{ currentMonthKey }}
        </h2>
        <hr />
        <GameBoard></GameBoard>
        <hr />
        <CardsList></CardsList>
        <hr />
        {{ roomByCode }} <br />
      </template>
      <PlayersList
        :players="players"
        :room="roomByCode"
        v-if="players != undefined && roomByCode != undefined"
      >
      </PlayersList>
      <hr />
    </template>
    <template v-else>
      <FinishScreen
        :roundKey="currentRoundKey"
        :roomCode="roomCode"
        @reloadRound="reloadRound"
      ></FinishScreen>
    </template>
    <router-link :to="mainPath">{{ $t('buttons.toMainPage') }}</router-link>
  </div>
</template>

<script>
import { MAIN_PATH } from '@/pathVariables';
import roomByCode from '@/graphql/queries/rooms/roomByCode.gql';
import currentRoundByCode from '@/graphql/queries/rooms/currentRoundByCode.gql';
import roomUpdated from '@/graphql/subscriptions/rooms/roomUpdated.gql';
import currentRoundUpdated from '@/graphql/subscriptions/rooms/currentRoundUpdated.gql';
import PlayersList from '@/components/room/playground/PlayersList.vue';
import GameBoard from '@/components/room/playground/gameBoard/GameBoard.vue';
import CardsList from '@/components/room/playground/cardsList/CardsList.vue';
import WaitingScreen from '@/components/room/playground/WaitingScreen.vue';
import FinishScreen from '@/components/room/playground/FinishScreen.vue';

export default {
  name: 'RoomPlayground',
  components: {
    PlayersList,
    GameBoard,
    CardsList,
    WaitingScreen,
    FinishScreen,
  },
  data() {
    return { mainPath: MAIN_PATH, skip: false };
  },
  computed: {
    roomCode() {
      return this.$route.params.roomCode;
    },
    currentRoundKey() {
      if (this.currentRoundByCode != undefined) {
        return this.currentRoundByCode.key;
      }
      return '-';
    },
    currentMonthKey() {
      if (this.currentRoundByCode != undefined) {
        if (this.currentRoundByCode.currentMonth != undefined) {
          return this.currentRoundByCode.currentMonth.key;
        }
      }
      return '-';
    },
    flow() {
      if (this.roomByCode != undefined) {
        if (this.roomByCode.flow != undefined) {
          return this.roomByCode.flow.title;
        }
      }
      return '-';
    },
    players() {
      if (this.roomByCode != undefined) {
        if (this.roomByCode.roomparticipantSet != undefined) {
          return this.roomByCode.roomparticipantSet;
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
  },
  methods: {
    async reloadRound() {
      this.skip = true;
      await this.$apollo.queries.roomByCode.refresh();
      await this.$apollo.queries.currentRoundByCode.refresh();
      this.skip = false;
    },
  },
};
</script>

<style lang="scss" scoped></style>
