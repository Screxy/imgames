<template>
  <tbody>
    <TableBodyRow
      v-for="channel in channels"
      :key="channel.id"
      :channel="channel"
    ></TableBodyRow>
  </tbody>
</template>

<script>
import TableBodyRow from '@/components/room/playground/gameboard/TableBodyRow.vue';

export default {
  name: 'TableBody',
  components: {
    TableBodyRow,
  },
  props: {
    channels: {
      type: Array,
    },
  },
};
</script>

<style lang="scss" scoped></style>
