<template>
  <table border="1" cellspacing="0">
    <TableHead></TableHead>
    <TableBody :channels="channelsByCode"></TableBody>
    <TableFooter></TableFooter>
  </table>
</template>

<script>
import channelsByCode from '@/graphql/queries/gameboard/channelsByCode.gql';

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
  },
  computed: {
    roomCode() {
      return this.$route.params.roomCode;
    },
  },
};
</script>

<style lang="scss" scoped></style>
