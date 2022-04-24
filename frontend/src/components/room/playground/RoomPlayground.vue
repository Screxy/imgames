<template>
  <div>
    <h1>{{ $t('room.room') }} {{ roomCode }}</h1>
    <h2>
      {{ $t('room.mechanics') }} "{{ flow }}" / {{ $t('room.round') }} R{{
        currentRoundKey
      }}
      / {{ $t('room.month') }} M{{ currentMonthKey }}
    </h2>
    <hr />
    <PlayersList
      :players="players"
      :room="roomByCode"
      v-if="players != undefined && roomByCode != undefined"
    >
    </PlayersList>
    <hr />
    <GameBoard></GameBoard>
    <hr />
    <CardsList></CardsList>
    <hr />
    {{ roomByCode }} <br />
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

export default {
  name: 'RoomPlayground',
  components: {
    PlayersList,
    GameBoard,
    CardsList,
  },
  data() {
    return { mainPath: MAIN_PATH };
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
        updateQuery: (previousResult, { subscriptionData }) => {
          console.log(
            'previousResult',
            JSON.stringify(previousResult.roomByCode.currentRound.currentMonth)
          );
          console.log(
            'subscriptionData',
            JSON.stringify(
              subscriptionData.data.roomUpdated.currentRound.currentMonth
            )
          );
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
        updateQuery: (previousResult, { subscriptionData }) => {
          return {
            currentRoundByCode: subscriptionData.data.currentRoundUpdated,
          };
        },
      },
    },
  },
};
</script>

<style lang="scss" scoped></style>
