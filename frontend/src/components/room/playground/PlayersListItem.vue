<template>
  <div>
    {{ $t('room.player.player') }} {{ player.user.firstName }}
    {{ player.user.lastName }} (#{{ player.user.id }})
    <span v-if="ownerId == player.user.id">
      - {{ $t('room.player.roomOwner') }}</span
    >
  </div>
</template>

<script>
export default {
  name: 'PlayersListItem',
  props: {
    player: {
      type: Object,
      required: true,
    },
    ownerId: {
      type: Number,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped></style>
