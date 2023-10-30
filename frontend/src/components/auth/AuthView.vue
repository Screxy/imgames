<template>
  <div class="auth-page">
    <TopBar :type="'auth'"></TopBar>
    <div class="auth-view default-background">
      <div class="normal-border-box auth-box">
        <h1>{{ $t('auth.authHeader') }}</h1>
        <form @submit.prevent>
          <TextInput
            :label="$t('auth.emailLabel')"
            :placeholder="$t('auth.emailLabel')"
            :autocomplete="'email'"
            v-model="email"
          />
          <TextInput
            :label="$t('auth.passwordLabel')"
            :placeholder="$t('auth.passwordLabel')"
            :type="'password'"
            :autocomplete="'current-password'"
            v-model="password"
          />
          <SubmitButton class="enter-button" @click="tryLogIn">
            {{ $t('auth.enterButton') }}
          </SubmitButton>
        </form>
        <p style="color: red" v-if="errors">
          {{ $t('auth.wrongCredentialsText') }}
        </p>
        {{ $t('auth.signUpText') }}
        <SubmitButton
          class="sign-up-button"
          :type="'dark-text'"
          @click="$router.push(SIGN_UP_PATH)"
        >
          {{ $t('auth.signUpButton') }}
        </SubmitButton>
        <SubmitButton
          class="sign-up-button"
          :type="'dark-text'"
          @click="$router.push(RESET_PASSWORD_PATH)"
        >
          {{ $t('auth.resetPasswordButton') }}
        </SubmitButton>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {
  MAIN_PATH,
  SIGN_UP_PATH,
  RESET_PASSWORD_PATH,
} from '@/router/pathVariables'
import TextInput from '@/components/ui/TextInput.vue'
import SubmitButton from '@/components/ui/SubmitButton.vue'
import TopBar from '@/components/ui/TopBar.vue'
import login from '@/graphql/mutations/login'
import { verifyAuth } from '@/router/router'
import { useStore } from '@/stores/store'
import { ref } from 'vue'
import { useMutation } from '@vue/apollo-composable'
import gql from 'graphql-tag'

const store = useStore()
const email = ref('')
const password = ref('')
const errors = ref(false)
const { mutate } = useMutation(login)
const tryLogIn = async () => {
  store.isLoading = true
  try {
    const data = await mutate({
      email: email.value,
      password: password.value,
    })
    store.isAuthenticated = true
    store.gotVerifiedAuth = true
    
    console.log(data?.data.login.token)
  } catch (error) {
    console.error(error)
    errors.value = true
  } finally {
    store.isLoading = false
  }
}
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
