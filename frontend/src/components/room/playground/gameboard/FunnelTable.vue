<template>
  <table border="1" cellspacing="0">
    <TableHead :stages="stagesByCode"></TableHead>
    <TableBody :stages="stagesByCode" :channels="channelsByCode"></TableBody>
    <TableFooter :stages="stagesByCode"></TableFooter>
  </table>
</template>

<script>
import channelsByCode from '@/graphql/queries/gameboard/channelsByCode.gql';
import stagesByCode from '@/graphql/queries/gameboard/stagesByCode.gql';

import TableBody from '@/components/room/playground/gameboard/TableBody.vue';
import TableFooter from '@/components/room/playground/gameboard/TableFooter.vue';
import TableHead from '@/components/room/playground/gameboard/TableHead.vue';

export default {
  name: 'FunnelTable',
  components: {
    TableHead,
    TableBody,
    TableFooter,
  },
  apollo: {
    channelsByCode: {
      query: channelsByCode,
      variables() {
        return {
          code: this.roomCode,
        };
      },
    },
    stagesByCode: {
      query: stagesByCode,
      variables() {
        return {
          code: this.roomCode,
        };
      },
    },
  },
  computed: {
    roomCode() {
      return this.$route.params.roomCode;
    },
  },
};
</script>

<style lang="scss" scoped></style>
