<template>
  <div class="finish-screen scrollable">
    <div>
      <h2>{{ $t('room.roundFinishedHeader', { round: `R${roundKey}` }) }}</h2>
      {{ winnersFromCurrentRound }}
      <template v-if="isRoomOwner">
        <div class="next-round-btn">
          <SubmitButton :type="'bg-green'" @click="reStartRound">{{
            $t('room.reStartRoundButton', { nextRound: `R${roundKey + 1}` })
          }}</SubmitButton>
        </div>
      </template>
    </div>
    <div class="history-row">
      <template v-for="(monthKey, index) in monthKeys">
        <div class="history-row-item" :key="monthKey + '-' + index + '!div'">
          <small v-if="monthKey == null" :key="monthKey + '-' + index + '!'">{{
            $t('room.startMonth')
          }}</small>
          <small v-if="monthKey != null" :key="monthKey + '-' + index + '!!'"
            >{{ $t('room.month') }} №{{ monthKey }}</small
          >
          <FinishFunnelTable
            :computedChannelsByCode="computedDataForMonth(monthKey)"
            :channelsByCode="channelsByCode"
            :stagesByCode="stagesByCode"
            :key="'fft--' + index"
            :monthKey="monthKey"
          ></FinishFunnelTable>
          <FinishTurnChoices
            v-if="computedTurnForMonth(monthKey != null ? monthKey : 0) != null"
            :turn="computedTurnForMonth(monthKey != null ? monthKey : 0)"
            :monthKey="monthKey != null ? monthKey : 0"
            :key="'ftc--' + monthKey + '-' + index"
          ></FinishTurnChoices>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import isRoomOwner from '@/graphql/queries/rooms/isRoomOwner.gql';
import SubmitButton from '@/components/ui/SubmitButton.vue';
import FinishFunnelTable from '@/components/room/playground/FinishFunnelTable.vue';
import reStartRound from '@/graphql/mutations/rooms/reStartRound.gql';
import turnsFromCurrentRound from '@/graphql/queries/rooms/turnsFromCurrentRound.gql';
import allComputedMonthsByCode from '@/graphql/queries/gameBoard/allComputedMonthsByCode.gql';
import channelsByCode from '@/graphql/queries/gameBoard/channelsByCode.gql';
import stagesByCode from '@/graphql/queries/gameBoard/stagesByCode.gql';
import winnersFromCurrentRound from '@/graphql/queries/rooms/winnersFromCurrentRound.gql';
import FinishTurnChoices from '@/components/room/playground/FinishTurnChoices.vue';

export default {
  name: 'FinishScreen',
  components: {
    SubmitButton,
    FinishFunnelTable,
    FinishTurnChoices,
  },
  props: {
    roundKey: {
      type: Number,
      required: true,
    },
    roomCode: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      monthKeys: [],
    };
  },
  apollo: {
    winnersFromCurrentRound: {
      query: winnersFromCurrentRound,
      variables() {
        return {
          code: this.roomCode,
        };
      },
    },
    channelsByCode: {
      query: channelsByCode,
      variables() {
        return {
          code: this.roomCode,
        };
      },
    },
    stagesByCode: {
      query: stagesByCode,
      variables() {
        return {
          code: this.roomCode,
        };
      },
    },
    isRoomOwner: {
      query: isRoomOwner,
      variables() {
        return {
          code: this.roomCode,
        };
      },
    },
    turnsFromCurrentRound: {
      query: turnsFromCurrentRound,
      variables() {
        return {
          code: this.roomCode,
        };
      },
    },
    allComputedMonthsByCode: {
      query: allComputedMonthsByCode,
      variables() {
        return {
          code: this.roomCode,
        };
      },
    },
  },
  methods: {
    reStartRound() {
      this.$apollo
        .mutate({
          mutation: reStartRound,
          variables: {
            code: this.roomCode,
          },
        })
        .then(() => {})
        .catch((e) => {
          console.log(e);
        })
        .finally(() => {
          this.$emit('reloadRound');
        });
    },
    computedDataForMonth(monthKey) {
      return this.allComputedMonthsByCode.filter(
        (el) => el.monthKey == monthKey
      );
    },
    computedTurnForMonth(monthKey) {
      return this.turnsFromCurrentRound.find((el) => el.month.key == monthKey);
    },
  },
  watch: {
    allComputedMonthsByCode() {
      this.$store.commit('CLEAN_CHOSEN_CARD');
      this.monthKeys = [
        ...new Set(this.allComputedMonthsByCode.map((el) => el.monthKey)),
      ].sort((a, b) => {
        if (a > b) return 1;
        if (b == null || a < b) return -1;
        return 0;
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.finish-screen {
  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 3;
  overflow-y: auto;
}

.next-round-btn {
  margin-top: 16px;
  margin-bottom: 16px;
  position: sticky;
  top: 1rem;
  z-index: 1000;
}
.history-row {
  display: flex;
  flex-direction: column;
  margin-bottom: 1rem;

  &-item {
    margin: auto;
  }
}
</style>
