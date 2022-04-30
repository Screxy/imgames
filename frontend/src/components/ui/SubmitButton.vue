<template>
  <button
    @click="sendClick"
    :disabled="disabled"
    :class="{ 'light-text': type == 'light-text' }"
  >
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'SubmitButton',
  props: {
    disabled: {
      type: Boolean,
      required: false,
    },
    type: {
      type: String,
    },
  },
  methods: {
    sendClick() {
      this.$emit('click');
    },
  },
};
</script>

<style lang="scss" scoped>
@import '@/scss/_variables.scss';

button {
  cursor: pointer;
}

.light-text {
  background-color: transparent;
  border: 0;
  color: $light_text_color;
  font-family: $primary_font;
  font-size: 1rem;

  &:hover {
    text-decoration: underline;
  }
}
</style>
