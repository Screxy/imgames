<template>
  <div>
    <h1>{{ $t('room.room') }} {{ roomCode }}</h1>
    <router-link :to="mainPath">{{ $t('buttons.toMainPage') }}</router-link>
  </div>
</template>

<script>
import { MAIN_PATH } from '@/pathVariables';
export default {
  name: 'RoomPlayground',
  data() {
    return { mainPath: MAIN_PATH };
  },
  computed: {
    roomCode() {
      return this.$route.params.roomCode;
    },
  },
};
</script>

<style lang="scss" scoped></style>
