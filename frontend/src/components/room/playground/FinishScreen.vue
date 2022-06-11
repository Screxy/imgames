<template>
  <div class="finish-screen">
    <h2>{{ $t('room.roundFinishedHeader', { round: `R${roundKey}` }) }}</h2>
    <!-- <div>
      {{ turnsFromCurrentRound }}
    </div> -->

    <!-- <FinishFunnelTable
      :computedChannelsByCode="computedDataForMonth(0)"
      :channelsByCode="channelsByCode"
      :stagesByCode="stagesByCode"
      :monthKey="monthKey"
    ></FinishFunnelTable> -->
    <template v-for="(monthKey, index) in monthKeys">
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
    </template>
    <template v-if="isRoomOwner">
      <SubmitButton :type="'bg-green'" @click="reStartRound">{{
        $t('room.reStartRoundButton', { nextRound: `R${roundKey + 1}` })
      }}</SubmitButton>
    </template>
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

export default {
  name: 'FinishScreen',
  components: {
    SubmitButton,
    FinishFunnelTable,
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
  },
  watch: {
    allComputedMonthsByCode() {
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

<style lang="scss" scoped></style>
