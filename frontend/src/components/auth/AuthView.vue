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
import TextInput from '@/components/ui/TextInput.vue';
import SubmitButton from '@/components/ui/SubmitButton.vue';
import LogIn from '@/graphql/mutations/login.gql';

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
      this.$apollo
        .mutate({
          mutation: LogIn,
          variables: {
            email: this.email,
            password: this.password,
          },
        })
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped></style>
