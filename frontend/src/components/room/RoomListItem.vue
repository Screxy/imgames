<template>
  <div>{{ $t('room.room') }} {{ room.code }}</div>
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
