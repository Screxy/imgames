<template>
  <thead>
    <tr>
      <TableHeadCell
        :textContent="$t('room.gameboard.channelsTitle')"
      ></TableHeadCell>
      <TableHeadCell
        :textContent="$t('room.gameboard.trafficTitle')"
      ></TableHeadCell>
      <!-- TODO: add double column v-for -->
      <TableHeadCell :textContent="$t('room.gameboard.total')"></TableHeadCell>
    </tr>
  </thead>
</template>

<script>
import TableHeadCell from '@/components/room/playground/gameboard/TableHeadCell.vue';

export default {
  name: 'TableHead',
  components: {
    TableHeadCell,
  },
};
</script>

<style lang="scss" scoped></style>
