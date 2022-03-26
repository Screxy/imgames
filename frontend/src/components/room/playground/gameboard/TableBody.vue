<template>
  <tbody>
    <TableBodyRow
      v-for="channel in channels"
      :key="channel.id"
      :channel="channel"
      :stages="stages"
      :data="rowData(channel.id)"
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
    stages: {
      type: Array,
    },
    data: {
      type: Array,
    },
  },
  methods: {
    rowData(channelId) {
      console.log(channelId);
      console.log(this.data);
      let dataObject = this.data.find((el) => {
        console.log(el.channel.id, channelId, el.channel.id == channelId);
        return +el.channel.id == +channelId;
      });
      console.log(dataObject);
      if (dataObject != undefined) {
        console.log(dataObject.data);
        return dataObject.data;
      }
      return {};
    },
  },
};
</script>

<style lang="scss" scoped></style>
