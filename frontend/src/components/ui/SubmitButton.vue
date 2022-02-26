<template>
  <button @click="sendClick"><slot></slot></button>
</template>

<script>
export default {
  name: 'SubmitButton',
  methods: {
    sendClick() {
      this.$emit('click');
    },
  },
};
</script>

<style lang="scss" scoped></style>
