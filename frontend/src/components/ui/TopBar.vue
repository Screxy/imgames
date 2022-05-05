<template>
  <div id="top-bar">
    <Logo></Logo>
    <div class="menu-block" v-if="type == 'playground'">
      <div class="left-block">
        <div class="menu-link menu-link-bold">
          {{ $t('room.room') }} {{ roomCode }} / {{ $t('room.round') }} R{{
            roomRound
          }}
          / {{ $t('room.month') }} M{{ roomMonth }}
        </div>
      </div>
      <div class="right-block">
        <router-link class="menu-link" :to="mainPath"
          >{{ $t('buttons.toMainPage') }} →</router-link
        >
      </div>
    </div>
    <div class="menu-block" v-else>
      <div class="left-block"></div>
      <div class="right-block">
        <LogOutButton class="menu-link"></LogOutButton>
      </div>
    </div>
  </div>
</template>

<script>
import { MAIN_PATH } from '@/pathVariables';
import Logo from '@/components/ui/Logo.vue';
import LogOutButton from '@/components/auth/LogOutButton.vue';

export default {
  name: 'TopBar',
  components: { Logo, LogOutButton },
  props: {
    type: {
      type: String,
    },
    roomCode: {
      type: String,
    },
    roomRound: {
      type: Number,
    },
    roomMonth: {
      type: Number,
    },
  },
  data() {
    return {
      mainPath: MAIN_PATH,
    };
  },
};
</script>

<style lang="scss" scoped>
@import '@/scss/_variables.scss';

#top-bar {
  background-color: $main_dark_bg_color;
  display: flex;
  height: 48px;

  .menu-block {
    display: flex;
    justify-content: space-between;
    font-family: $primary_font;
    width: 100%;

    .left-block,
    .right-block {
      display: flex;

      a {
        &:hover {
          text-decoration: underline;
        }
      }

      .menu-link {
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        padding: 0 1rem;
        color: $light_text_color;
        font-size: 1rem;

        &-bold {
          font-family: $primary_font_bold;
        }
      }
    }
  }
}
</style>
