<template>
  <tfoot>
    <tr>
      <td>
        <i>{{ $t('room.gameboard.total') }}</i>
      </td>
      <CardinalNumberCell :value="0"></CardinalNumberCell>
      <template v-for="(stage, index) in stages">
        <PercentCell :key="stage.id + '.1'" :value="0"></PercentCell>
        <CardinalNumberCell
          :key="stage.id + '.2'"
          :value="0"
          v-if="index != stages.length - 1"
        ></CardinalNumberCell>
      </template>
      <CardinalNumberCell :value="0"></CardinalNumberCell>
    </tr>
  </tfoot>
</template>

<script>
import CardinalNumberCell from '@/components/room/playground/gameboard/CardinalNumberCell.vue';
import PercentCell from '@/components/room/playground/gameboard/PercentCell.vue';

export default {
  name: 'TableFooter',
  components: {
    CardinalNumberCell,
    PercentCell,
  },
  props: {
    stages: {
      type: Array,
    },
  },
};
</script>

<style lang="scss" scoped></style>
