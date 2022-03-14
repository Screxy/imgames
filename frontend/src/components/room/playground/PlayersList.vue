<template>
  <div>
    <h3>{{ $t('room.player.playersList') }}</h3>
    <PlayersListItem
      v-for="player in players"
      :key="player.id"
      :player="player"
      :ownerId="roomOwnerId"
    ></PlayersListItem>
  </div>
</template>

<script>
import PlayersListItem from '@/components/room/playground/PlayersListItem.vue';

export default {
  name: 'PlayersList',
  components: {
    PlayersListItem,
  },
  props: {
    players: {
      type: Array,
      required: true,
    },
    room: {
      type: Array,
      required: true,
    },
  },
  computed: {
    roomOwnerId() {
      if (this.room.roomOwner != undefined) {
        if (this.room.roomOwner.id != undefined) {
          return this.room.roomOwner.id;
        }
      }
      return {};
    },
  },
};
</script>

<style lang="scss" scoped></style>
