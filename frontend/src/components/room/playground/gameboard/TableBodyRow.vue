<template>
  <tr>
    <ChannelTitleCell :title="channel.name"></ChannelTitleCell>
    <CardinalNumberCell :value="+data[0]"></CardinalNumberCell>
    <template v-for="(stage, index) in stages">
      <PercentCell
        :key="stage.id + '.1'"
        :value="+data[1 + index * 2]"
      ></PercentCell>
      <CardinalNumberCell
        :key="stage.id + '.2'"
        :value="+data[2 + index * 2]"
        v-if="index != stages.length - 1"
      ></CardinalNumberCell>
    </template>
    <CardinalNumberCell :value="+data[data.length - 1]"></CardinalNumberCell>
  </tr>
</template>

<script>
import ChannelTitleCell from '@/components/room/playground/gameboard/ChannelTitleCell.vue';
import CardinalNumberCell from '@/components/room/playground/gameboard/CardinalNumberCell.vue';
import PercentCell from '@/components/room/playground/gameboard/PercentCell.vue';

export default {
  name: 'TableBodyRow',
  components: {
    ChannelTitleCell,
    CardinalNumberCell,
    PercentCell,
  },
  props: {
    channel: {
      type: Object,
    },
    stages: {
      type: Array,
    },
    data: {
      type: Array,
    },
  },
};
</script>

<style lang="scss" scoped></style>
