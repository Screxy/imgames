<template>
  <tr>
    <ChannelTitleCell :title="channel.name"></ChannelTitleCell>
    <CardinalNumberCell :value="+channel.defaultValue"></CardinalNumberCell>
  </tr>
</template>

<script>
import ChannelTitleCell from '@/components/room/playground/gameboard/ChannelTitleCell.vue';
import CardinalNumberCell from '@/components/room/playground/gameboard/CardinalNumberCell.vue';

export default {
  name: 'TableBodyRow',
  components: {
    ChannelTitleCell,
    CardinalNumberCell,
  },
  props: {
    channel: {
      type: Object,
    },
  },
};
</script>

<style lang="scss" scoped></style>
