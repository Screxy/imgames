<template>
  <div>
    <h2>{{ $t('room.connectRoom') }}</h2>
    <div class="normal-border-box connect-room-form">
      <TextInput
        :label="$t('room.roomCode')"
        :name="'roomCode'"
        :placeholder="$t('room.roomCode')"
        :disabled="formLoading"
        :type="'text'"
        @input="roomCode = $event"
      ></TextInput>
      <SubmitButton
        :type="'bg-green'"
        :disabled="formLoading"
        @click="joinRoom"
      >
        {{ $t('buttons.connect') }}
      </SubmitButton>
    </div>
  </div>
</template>

<script>
import TextInput from '@/components/ui/TextInput.vue';
import SubmitButton from '@/components/ui/SubmitButton.vue';

export default {
  name: 'ConnectRoomView',
  components: {
    TextInput,
    SubmitButton,
  },
  data() {
    return {
      roomCode: '',
      formLoading: false,
    };
  },
  methods: {
    joinRoom() {
      console.log('!!!');
    },
  },
};
</script>

<style lang="scss" scoped>
h2 {
  text-align: center;
}
.connect-room-form {
  padding: 1rem;
  & .user-input {
    & input {
      width: 100%;
      box-sizing: border-box;
    }
  }
  & button {
    width: 100%;
  }
}
</style>
