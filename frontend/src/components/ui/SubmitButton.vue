<template>
  <button @click="sendClick" :disabled="disabled"><slot></slot></button>
</template>

<script>
export default {
  name: 'SubmitButton',
  props: {
    disabled: {
      type: Boolean,
      required: false,
    },
  },
  methods: {
    sendClick() {
      this.$emit('click');
    },
  },
};
</script>

<style lang="scss" scoped></style>
