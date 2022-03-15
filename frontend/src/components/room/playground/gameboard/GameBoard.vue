<template>
  <div>
    <h3>{{ $t('room.gameboard.gameboard') }}</h3>
    <FunnelTable></FunnelTable>
  </div>
</template>

<script>
import FunnelTable from '@/components/room/playground/gameboard/FunnelTable.vue';

export default {
  name: 'GameBoard',
  components: {
    FunnelTable,
  },
};
</script>

<style lang="scss" scoped></style>
