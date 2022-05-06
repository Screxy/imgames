<template>
  <div class="user-input">
    <label :for="name">{{ label }}</label>
    <input
      :id="name"
      :name="name"
      :type="type"
      :placeholder="placeholder"
      :autocomplete="autocomplete"
      :disabled="disabled"
      v-model="inputModel"
      @input="sendInput"
    />
  </div>
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
    predefined: {
      type: undefined,
      default: '',
    },
    label: {
      type: String,
    },
    name: {
      type: String,
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

<style lang="scss" scoped>
@import '@/scss/_variables.scss';

label,
input {
  font-family: $primary_font;
  color: $dark_text_color;
}
input {
  padding: 0.5rem 1rem;
  border-radius: 8px;
  border: none;
}
.user-input {
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
}
</style>
