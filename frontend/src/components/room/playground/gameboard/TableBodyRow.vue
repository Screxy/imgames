<template>
  <tr>
    <ChannelTitleCell :title="channel.name"></ChannelTitleCell>
    <CardinalNumberCell :value="+channel.defaultValue"></CardinalNumberCell>
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
  },
};
</script>

<style lang="scss" scoped></style>
