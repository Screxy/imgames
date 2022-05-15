<template>
  <div>
    <div class="sign-up-page">
      <TopBar :type="'sign-up'"></TopBar>
      <div class="sign-up-view default-background">
        <div class="normal-border-box sign-up-box">
          <h1>{{ $t('auth.signUpHeader') }}</h1>
          <form @submit.prevent>
            <TextInput
              :label="$t('auth.emailLabel')"
              :placeholder="$t('auth.emailLabel')"
              :autocomplete="'email'"
              @input="email = $event"
            ></TextInput>
            <TextInput
              :label="$t('auth.passwordLabel')"
              :placeholder="$t('auth.passwordLabel')"
              :autocomplete="'new-password'"
              @input="password = $event"
            ></TextInput>
            <TextInput
              :label="$t('auth.firstNameLabel')"
              :placeholder="$t('auth.firstNameLabel')"
              :autocomplete="'first-name'"
              @input="firstName = $event"
            ></TextInput>
            <TextInput
              :label="$t('auth.lastNameLabel')"
              :placeholder="$t('auth.lastNameLabel')"
              :autocomplete="'family-name'"
              @input="lastName = $event"
            ></TextInput>
            <SubmitButton class="sign-up-button" @click="trySignUp">{{
              $t('auth.signUpButton')
            }}</SubmitButton>
          </form>
          {{ $t('auth.enterText') }}
          <SubmitButton
            class="enter-button"
            :type="'dark-text'"
            @click="$router.push(authPath)"
            >{{ $t('auth.enterButton') }}</SubmitButton
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TopBar from '@/components/ui/TopBar.vue';
import TextInput from '@/components/ui/TextInput.vue';
import SubmitButton from '@/components/ui/SubmitButton.vue';
import { AUTH_PATH } from '@/pathVariables.js';

export default {
  name: 'SignUpView',
  components: {
    TopBar,
    TextInput,
    SubmitButton,
  },
  data() {
    return {
      authPath: AUTH_PATH,
      email: '',
      password: '',
      firstName: '',
      lastName: '',
    };
  },
  methods: {
    trySignUp() {},
  },
};
</script>

<style lang="scss" scoped>
.sign-up-page {
  height: 100vh;
  & .sign-up-view {
    height: calc(100vh - 48px);
    width: 100vw;
    display: flex;
    & .sign-up-box {
      margin: auto;
      max-width: 380px;
      width: 40%;
      padding: 1rem;
      box-sizing: border-box;
      h1 {
        padding-top: 0;
        padding-bottom: 1rem;
      }
      .sign-up-button {
        width: 100%;
        margin-bottom: 1rem;
      }
      .enter-button {
        padding: 0;
      }
    }
  }
}
</style>
