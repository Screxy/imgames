<template>
  <input
    :type="type"
    :placeholder="placeholder"
    :autocomplete="autocomplete"
    :disabled="disabled"
    v-model="inputModel"
    @input="sendInput"
  />
</template>

<script>
export default {
  name: 'TextInput',
  data() {
    return {
      inputModel: '',
    };
  },
  props: {
    placeholder: {
      type: String,
      required: true,
    },
    autocomplete: {
      type: String,
      default: 'false',
    },
    type: {
      type: String,
      default: 'text',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    sendInput() {
      this.$emit('input', this.inputModel);
    },
  },
};
</script>

<style lang="scss" scoped></style>
