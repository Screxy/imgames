<template>
  <tfoot>
    <tr>
      <td>
        <i>{{ $t('room.gameBoard.total') }}</i>
      </td>
      <CardinalNumberCell :value="+data[0]"></CardinalNumberCell>
      <template v-for="(stage, index) in stages">
        <PercentCell
          :key="stage.id + '.1'"
          :value="+data[1 + 2 * index]"
          :isHide="true"
        ></PercentCell>
        <CardinalNumberCell
          :key="stage.id + '.2'"
          :value="+data[2 + 2 * index]"
          v-if="index != stages.length - 1"
        ></CardinalNumberCell>
      </template>
      <CardinalNumberCell :value="+data[data.length - 1]"></CardinalNumberCell>
    </tr>
  </tfoot>
</template>

<script>
import CardinalNumberCell from '@/components/room/playground/gameBoard/CardinalNumberCell.vue';
import PercentCell from '@/components/room/playground/gameBoard/PercentCell.vue';

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
    data: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped></style>
