<template>
  <div class="players-list-item normal-border-box">
    <img src="@/assets/no_avatar.svg" alt="Аватар" />
    {{ player.user.firstName }}
    {{ player.user.lastName }}
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

<style lang="scss" scoped>
@import '@/scss/_variables.scss';

.players-list-item {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 8px;
  font-family: $primary_font;
  color: $dark_text_color;
  text-align: center;
  font-size: 14px;

  img {
    height: 38px;
  }
}
</style>
