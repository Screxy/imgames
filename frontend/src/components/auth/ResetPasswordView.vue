<template>
  <div class="auth-page">
    <TopBar :type="'auth'"></TopBar>
    <div class="auth-view default-background" v-if='!success'>
      <div class="normal-border-box auth-box">
        <h1>{{ $t('auth.resetPasswordHeader') }}</h1>
        <form @submit.prevent>
          <TextInput
            :label="$t('auth.emailLabel')"
            :placeholder="$t('auth.emailLabel')"
            :autocomplete="'email'"
            @input="email = $event"
          ></TextInput>
          <SubmitButton class="enter-button" @click="resetPassword">{{
            $t('auth.resetPasswordSendButton')
          }}</SubmitButton>
        </form>
      </div>
    </div>
    <div class="auth-view default-background" v-else>
      <div class="normal-border-box auth-box">
        <h1>Вам на почту было отправлено письмо для восстановления пароля</h1>
        <SubmitButton
            class="sign-up-button"
            :type="'dark-text'"
            @click="$router.push(authPath)"
            >Вернуться на главную</SubmitButton
        >
      </div>
    </div>
  </div>
</template>

<script>
import { MAIN_PATH, AUTH_PATH } from '@/pathVariables.js';
import TextInput from '@/components/ui/TextInput.vue';
import SubmitButton from '@/components/ui/SubmitButton.vue';
import TopBar from '@/components/ui/TopBar.vue';
import resetPassword from '@/graphql/mutations/resetPassword.gql';

export default {
  name: 'ResetPassword',
  components: {
    TextInput,
    SubmitButton,
    TopBar,
  },
  data() {
    return {
      email: '',
      authPath: AUTH_PATH,
      success: false,
    };
  },
  methods: {
    resetPassword() {
      this.$store.commit('START_LOADING');
      this.$apollo
        .mutate({
          mutation: resetPassword,
          variables: {
            email: this.email,
          },
        })
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error(error);
        })
        .finally(() => {
          this.success = true
          this.$store.commit('STOP_LOADING');
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.auth-page {
  height: 100vh;
  & .auth-view {
    height: calc(100vh - 48px);
    width: 100vw;
    display: flex;
    & .auth-box {
      margin: auto;
      max-width: 380px;
      width: 40%;
      padding: 1rem;
      box-sizing: border-box;
      h1 {
        padding-top: 0;
        padding-bottom: 1rem;
      }
      .enter-button {
        width: 100%;
        margin-bottom: 1rem;
      }
      .sign-up-button {
        padding: 0;
      }
    }
  }
}
@media screen and (max-width: 610px) {
  .auth-page {
    & .auth-view {
      & .auth-box {
        width: 70%;
      }
    }
  }
}
@media screen and (max-width: 380px) {
  .auth-page {
    & .auth-view {
      & .auth-box {
        width: 96%;

        & h1 {
          font-size: 24px;
        }
      }
    }
  }
}
</style>
