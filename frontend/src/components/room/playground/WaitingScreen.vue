<template>
  <div>
    <p>{{ $t('room.waitingHeader') }}</p>
    <template v-if="isRoomOwner">
      <p>{{ $t('room.waitingTextForOwner') }}</p>
      <SubmitButton @click="startRound">{{
        $t('room.startRoundButton')
      }}</SubmitButton>
    </template>
  </div>
</template>

<script>
import SubmitButton from '@/components/ui/SubmitButton.vue';
import startRound from '@/graphql/mutations/rooms/startRound.gql';
import isRoomOwner from '@/graphql/queries/rooms/isRoomOwner.gql';

export default {
  name: 'WaitingScreen',
  components: {
    SubmitButton,
  },
  props: {
    roomCode: {
      type: String,
      required: true,
    },
    roomOwner: {
      type: Object,
    },
  },
  apollo: {
    isRoomOwner: {
      query: isRoomOwner,
      variables() {
        return {
          code: this.roomCode,
        };
      },
    },
  },
  methods: {
    startRound() {
      this.$apollo
        .mutate({
          mutation: startRound,
          variables: {
            code: this.roomCode,
          },
        })
        .then(() => {})
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>

<style lang="scss" scoped></style>
