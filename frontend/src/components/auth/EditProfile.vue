<template>
    <div>
      <div class="sign-up-page">
        <TopBar
            type="editProfile"
        ></TopBar>
        <div class="sign-up-view default-background">
          <div class="normal-border-box sign-up-box">
            <template>
              <h1>{{ $t('profile.editHeader') }}</h1>
              <form @submit.prevent>
                <TextInput
                  :label="$t('auth.emailLabel')"
                  :placeholder="$t('auth.emailLabel')"
                  :autocomplete="'email'"
                  :isAnyError="$v.form.email.$anyError"
                  :isRequiredError="
                    !$v.form.email.required && $v.form.email.$anyDirty
                  "
                  :value="profile.email"
                  :disabled="true"
                  @input="setEmail($event)"
                ></TextInput>
                <TextInput
                  :label="$t('auth.firstNameLabel')"
                  :placeholder="$t('auth.firstNameLabel')"
                  :autocomplete="'first-name'"
                  :isAnyError="$v.form.firstName.$anyError"
                  :isRequiredError="
                    !$v.form.firstName.required && $v.form.firstName.$anyDirty
                  "
                  :value="profile.firstName"
                  :disabled="isLoading"
                  @input="setFirstName($event)"
                ></TextInput>
                <TextInput
                  :label="$t('auth.lastNameLabel')"
                  :placeholder="$t('auth.lastNameLabel')"
                  :autocomplete="'family-name'"
                  :isAnyError="$v.form.lastName.$anyError"
                  :isRequiredError="
                    !$v.form.lastName.required && $v.form.lastName.$anyDirty
                  "
                  :value="profile.lastName"
                  :disabled="isLoading"
                  @input="setLastName($event)"
                ></TextInput>
                <div class="errors">
                  <div class="error-message" v-if="errorsContains('commonError')">
                    Возникла ошибка. Попробуйте повторить позднее.
                  </div>
                </div>
                <SubmitButton
                  class="sign-up-button"
                  :disabled="isLoading || isSaveButtonDisabled"
                  @click="trySave"
                  type="bg-green"
                  >{{ $t('profile.save') }}</SubmitButton
                >
                <SubmitButton
                  class="sign-up-button"
                  :disabled="isLoading"
                  @click="$router.push('/')"
                  >{{ $t('profile.discard') }}</SubmitButton
                >
              </form>
            </template> 
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
  import { required } from 'vuelidate/lib/validators';
  import profile from '@/graphql/queries/profile.gql';
  import editProfile from '@/graphql/mutations/editProfile.gql';
  
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
        form: {
          email: '',
          firstName: '',
          lastName: '',
        },
        isLoading: false,
        isSuccess: false,
        errors: [],
        noChanges: true,
      };
    },
    apollo: {
        profile: {
            query: profile,
        }
    },
    methods: {
      setEmail(email) {
        this.noChanges = false;
        this.form.email = email;
        this.$v.form.email.$model = email;
        this.$v.form.email.$touch();
        this.errors = [];
        return email;
      },
      setFirstName(firstName) {
        this.noChanges = false;
        this.form.firstName = firstName;
        this.$v.form.firstName.$model = firstName;
        this.$v.form.firstName.$touch();
        this.errors = [];
        return firstName;
      },
      setLastName(lastName) {
        this.noChanges = false;
        this.form.lastName = lastName;
        this.$v.form.lastName.$model = lastName;
        this.$v.form.lastName.$touch();
        this.errors = [];
        return lastName;
      },
      trySave() {
        this.$v.form.$touch();
        if (!this.$v.form.$anyError) {
          this.isLoading = true;
          this.$apollo
            .mutate({
              mutation: editProfile,
              variables: this.form,
            })
            .then((result) => {
              console.log('result', result.data.editProfile);
              if (result.data.editProfile.success) {
                this.$router.push('/');
              };
              this.errors = result.data.editProfile.errors;
            })
            .catch((error) => {
              console.log('error', error);
              this.errors = ['commonError'];
            })
            .finally(() => {
              this.isLoading = false;
            });
        }
      },
      errorsContains(error) {
        return this.errors.includes(error);
      },
    },
    validations: {
      form: {
        email: {
          required,
        },
        firstName: {
          required,
        },
        lastName: {
          required,
        },
      },
    },
    computed: {
      isSaveButtonDisabled() {
        return this.$v.form.$anyError || this.noChanges;
      },
    },
    watch: {
        profile(newValue) {
            this.form.email = newValue.email;
            this.form.firstName = newValue.firstName;
            this.form.lastName = newValue.lastName;
        }
    }
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
  