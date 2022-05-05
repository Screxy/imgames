<template>
  <div class="normal-border-box rooms-list-item">
    {{ $t('room.room') }} {{ room.code }}
    <router-link :to="'/r/' + room.code.toUpperCase()"
      >{{ $t('room.goToRoom') }}
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'RoomsListItem',
  props: {
    room: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
@import '@/scss/_variables.scss';

.rooms-list-item {
  font-family: $primary_font;
  color: $dark_text_color;
  margin-bottom: 0.5rem;
  padding: 1rem;
  margin-right: 1rem;
}
</style>
