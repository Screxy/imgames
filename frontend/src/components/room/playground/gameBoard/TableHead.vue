<template>
  <thead>
    <tr>
      <TableHeadCell
        :textContent="$t('room.gameBoard.channelsTitle')"
      ></TableHeadCell>
      <TableHeadCell
        :textContent="$t('room.gameBoard.trafficTitle')"
      ></TableHeadCell>
      <template v-for="(stage, index) in sortedStages">
        <TableHeadCell
          :textContent="$t('room.gameBoard.stageConversion') + ' ' + stage.name"
          :key="stage.id + '.1'"
        ></TableHeadCell>
        <TableHeadCell
          :textContent="stage.name"
          :key="stage.id + '.2'"
          v-if="index != stages.length - 1"
        ></TableHeadCell>
      </template>
      <!-- TODO: add double column v-for -->
      <TableHeadCell :textContent="$t('room.gameBoard.total')"></TableHeadCell>
    </tr>
  </thead>
</template>

<script>
import TableHeadCell from '@/components/room/playground/gameBoard/TableHeadCell.vue';

export default {
  name: 'TableHead',
  components: {
    TableHeadCell,
  },
  props: {
    stages: {
      type: Array,
    },
  },
  computed: {
    sortedStages() {
      if (Array.isArray(this.stages)) {
        return this.stages.sort(
          (a, b) => a.stageinsequence.place - b.stageinsequence.place
        );
      }
      return [];
    },
  },
};
</script>

<style lang="scss" scoped></style>
