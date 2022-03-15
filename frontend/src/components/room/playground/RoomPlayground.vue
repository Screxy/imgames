<template>
  <div>
    <h1>{{ $t('room.room') }} {{ roomCode }}</h1>
    <h2>{{ $t('room.round') }} R{{ currentRoundKey }}</h2>
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
    <!-- {{ roomByCode }} <br /> -->
    <router-link :to="mainPath">{{ $t('buttons.toMainPage') }}</router-link>
  </div>
</template>

<script>
import { MAIN_PATH } from '@/pathVariables';
import roomByCode from '@/graphql/queries/rooms/roomByCode.gql';
import PlayersList from '@/components/room/playground/PlayersList.vue';
import GameBoard from '@/components/room/playground/gameboard/GameBoard.vue';

export default {
  name: 'RoomPlayground',
  components: {
    PlayersList,
    GameBoard,
  },
  data() {
    return { mainPath: MAIN_PATH };
  },
  computed: {
    roomCode() {
      return this.$route.params.roomCode;
    },
    currentRoundKey() {
      if (this.roomByCode != undefined) {
        if (this.roomByCode.currentRound != undefined) {
          return this.roomByCode.currentRound.key;
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
    },
  },
};
</script>

<style lang="scss" scoped></style>
