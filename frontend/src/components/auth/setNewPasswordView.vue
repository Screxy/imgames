<template>
  <div class="auth-page">
    <TopBar :type="'auth'"></TopBar>
    <div class="auth-view default-background" v-if='!success'>
      <div class="normal-border-box auth-box">
        <h1>{{ $t('auth.setPasswordHeader') }}</h1>
        <form @submit.prevent>
          <TextInput
            :label="$t('auth.passwordLabel')"
            :placeholder="$t('auth.passwordLabel')"
            :type="'password'"
            :autocomplete="'current-password'"
            @input="password = $event"
          ></TextInput>
          <TextInput
            :label="$t('auth.passwordRepeatLabel')"
            :placeholder="$t('auth.passwordRepeatLabel')"
            :type="'password'"
            :autocomplete="'current-password'"
            @input="password2 = $event"
          ></TextInput>
          <p v-if=errors>Пароли должны совпадать</p>
          <SubmitButton class="enter-button" @click="setPassword">{{
            $t('auth.setNewPasswordSendButton')
          }}</SubmitButton>
        </form>
      </div>
    </div>
    <div v-else>
      <div class="normal-border-box auth-box">
        <h1>Ваш пароль был успешно изменен</h1>
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
import { AUTH_PATH } from '@/pathVariables.js';
import TextInput from '@/components/ui/TextInput.vue';
import SubmitButton from '@/components/ui/SubmitButton.vue';
import TopBar from '@/components/ui/TopBar.vue';
import resetPasswordConfirm from "@/graphql/mutations/resetPasswordConfirm.gql";

export default {
  name: 'SetNewPassword',
  components: {
    TextInput,
    SubmitButton,
    TopBar,
  },
  data() {
    return {
      password: '',
      password2: '',
      authPath: AUTH_PATH,
      success: false,
      errors: false,
    };
  },
  methods: {
    setPassword() {
      console.log(1)
      if (this.password == this.password2) {
        this.$store.commit('START_LOADING');
        this.$apollo
        .mutate({
          mutation: resetPasswordConfirm,
          variables: {
            token: this.$route.params.token,
            password: this.password
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
          this.errors = false
          this.$store.commit('STOP_LOADING');
        });
      }
      else {
        this.errors = true
      }
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
