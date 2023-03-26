<template>
    <div class="sign-up-page">
        <TopBar :type="'sign-up'"></TopBar>
        <div class="sign-up-view default-background" v-if='isSuccess'>
            <div class="normal-border-box sign-up-box">
                <h1>{{ $t('auth.signUpConfirmHeader') }}</h1>
                {{ $t('auth.signUpConfirmText') }}
                <SubmitButton
                    class="enter-button"
                    :type="'dark-text'"
                    @click="$router.push(authPath)"
                    >{{ $t('auth.enterButton') }}</SubmitButton
                >
            </div>
        </div>
        <div class="sign-up-view default-background" v-else>
            <div class="normal-border-box sign-up-box">
                <h1>{{ $t('auth.signUpConfirmErrorHeader') }}</h1>
            </div>
        </div>
    </div>
</template>  


<script>
import TopBar from '@/components/ui/TopBar.vue';
import TextInput from '@/components/ui/TextInput.vue';
import SubmitButton from '@/components/ui/SubmitButton.vue';
import { AUTH_PATH } from '@/pathVariables.js';
import confirmRegistration from '@/graphql/mutations/confirmRegistration.gql';

export default {
    name: 'SignUpConfirmView',
    components: {
        TopBar,
        TextInput,
        SubmitButton,
    },
    data() {
        return {
            authPath: AUTH_PATH,
            isSuccess: false,
            confirmationData: {},
            errors: {},
        }
    },
    mounted() {
        this.isLoading = true;
        this.$apollo
          .mutate({
            mutation: confirmRegistration,
            variables: this.$route.params,
          })
          .then((result) => {
            this.isSuccess = result.data.confirmRegistration.success;
            this.errors = result.data.confirmRegistration.errors;
          })
          .catch((error) => {
            console.log('error', error);
            this.errors = ['commonError'];
          })
          .finally(() => {
            this.isLoading = false;
          });
    }
}
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
      min-width: 320px;
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
      .errors {
        & * {
          margin: 0.25rem 0;
        }
      }
    }
  }
}

@media screen and (max-width: 360px) {
  .sign-up-page {
    & .sign-up-view {
      & .sign-up-box {
        min-width: unset;
        width: 94%;
        & h1 {
          font-size: 24px;
        }
      }
    }
  }
}
</style>
