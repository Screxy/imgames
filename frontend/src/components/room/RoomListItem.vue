<template>
  <div>
    {{ $t('room.room') }} {{ room.code }}
    <router-link :to="'/r/' + room.code.toUpperCase()">{{
      $t('room.goToRoom')
    }}</router-link>
  </div>
</template>

<script>
export default {
  name: 'RoomListItem',
  props: {
    room: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped></style>
