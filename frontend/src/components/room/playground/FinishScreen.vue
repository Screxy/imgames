<template>
  <div>
    <h2>{{ $t('room.roundFinishedHeader', { round: `R${roundKey}` }) }}</h2>
    <template v-if="isRoomOwner">
      <SubmitButton @click="reStartRound">{{
        $t('room.reStartRoundButton', { nextRound: `R${roundKey + 1}` })
      }}</SubmitButton>
    </template>
  </div>
</template>

<script>
import isRoomOwner from '@/graphql/queries/rooms/isRoomOwner.gql';
import SubmitButton from '@/components/ui/SubmitButton.vue';
import reStartRound from '@/graphql/mutations/rooms/reStartRound.gql';

export default {
  name: 'FinishScreen',
  components: {
    SubmitButton,
  },
  props: {
    roundKey: {
      type: Number,
      required: true,
    },
    roomCode: {
      type: String,
      required: true,
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
    reStartRound() {
      this.$apollo
        .mutate({
          mutation: reStartRound,
          variables: {
            code: this.roomCode,
          },
        })
        .then(() => {})
        .catch((e) => {
          console.log(e);
        })
        .finally(() => {
          this.$emit('reloadRound');
        });
    },
  },
};
</script>

<style lang="scss" scoped></style>
