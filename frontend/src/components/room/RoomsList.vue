<template>
  <div>
    <h2>{{ $t('room.roomsList') }}</h2>
    <div class="rooms-list">
      <RoomsListItem
        v-for="room in roomsInOrganization"
        :key="room.id"
        :room="room"
      ></RoomsListItem>
    </div>
  </div>
</template>

<script>
import RoomsListItem from '@/components/room/RoomsListItem.vue';
import roomsInOrganization from '@/graphql/queries/rooms/roomsInOrganization.gql';

export default {
  name: 'RoomList',
  components: {
    RoomsListItem,
  },
  apollo: {
    roomsInOrganization: {
      query: roomsInOrganization,
      variables() {
        return {
          subdomain: this.subdomain,
        };
      },
    },
  },
  computed: {
    subdomain() {
      return this.$store.state.subdomain;
    },
  },
};
</script>

<style lang="scss" scoped>
h2 {
  text-align: center;
}
</style>
