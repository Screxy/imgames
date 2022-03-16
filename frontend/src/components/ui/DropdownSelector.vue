<template>
  <select
    :disabled="disabled"
    v-model="inputModel"
    @input="sendInput"
    @change="sendInput"
  >
    <option
      :value="option.value"
      :key="index"
      v-for="(option, index) in options"
      :selected="option.value == predefined"
    >
      {{ option.label }}
    </option>
  </select>
</template>

<script>
export default {
  name: 'DropdownSelector',
  data() {
    return {
      inputModel: '',
    };
  },
  props: {
    options: {
      type: Array,
      required: true,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    predefined: {
      type: undefined,
      default: '',
    },
  },
  watch: {
    predefined(newValue) {
      this.inputModel = newValue;
      this.sendInput();
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
