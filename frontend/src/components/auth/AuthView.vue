<template>
  <div>
    <h1>Авторизация (AuthView)</h1>
    <form @submit.prevent>
      <TextInput
        :placeholder="'E-mail'"
        :autocomplete="'email'"
        @input="email = $event"
      ></TextInput>
      <TextInput
        :placeholder="'Пароль'"
        :type="'password'"
        :autocomplete="'current-password'"
        @input="password = $event"
      ></TextInput>
      <SubmitButton @click="tryLogIn">Отправить</SubmitButton>
    </form>
  </div>
</template>

<script>
import { MAIN_PATH } from '@/pathVariables.js';
import TextInput from '@/components/ui/TextInput.vue';
import SubmitButton from '@/components/ui/SubmitButton.vue';
import login from '@/graphql/mutations/login.gql';

export default {
  name: 'AuthView',
  components: { TextInput, SubmitButton },
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    tryLogIn() {
      this.$store.commit('START_LOADING');
      this.$apollo
        .mutate({
          mutation: login,
          variables: {
            email: this.email,
            password: this.password,
          },
        })
        .then((data) => {
          this.$store.commit('SET_IS_AUTHENTICATED', true);
          this.$store.commit('SET_GOT_VERIFIED_AUTH', true);
          this.$router.push(MAIN_PATH).catch((err) => {
            console.log(err);
          });
        })
        .catch((error) => {
          console.error(error);
        })
        .finally(() => {
          this.$store.commit('STOP_LOADING');
        });
    },
  },
};
</script>

<style lang="scss" scoped></style>
