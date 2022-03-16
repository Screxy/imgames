<template>
  <table border="1" cellspacing="0">
    <thead>
      <tr>
        <th>Заголовок</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Тело {{ channelsByCode }}</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td>Футер</td>
      </tr>
    </tfoot>
  </table>
</template>

<script>
import channelsByCode from '@/graphql/queries/gameboard/channelsByCode.gql';

export default {
  name: 'FunnelTable',
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
