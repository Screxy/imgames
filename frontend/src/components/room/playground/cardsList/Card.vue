<template>
  <div style="border: 1px solid black; width: 200px">
    <span v-if="selected">{{ $t('room.card.selectedCard') }}</span>
    <h4>{{ data.header }}</h4>
    <p>{{ data.shortDescription }}</p>
    <p>{{ data.cost }}₽</p>
    <SubmitButton @click="emitSelection()" v-if="!selected">{{
      $t('room.card.chooseCard')
    }}</SubmitButton>
    <SubmitButton @click="emitDeselect()" v-else>{{
      $t('room.card.deselectCard')
    }}</SubmitButton>
  </div>
</template>

<script>
import SubmitButton from '@/components/ui/SubmitButton.vue';

export default {
  name: 'Card',
  components: {
    SubmitButton,
  },
  props: {
    data: {
      type: Object,
      required: true,
    },
    selected: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    emitSelection() {
      this.$emit('select', this.data.id);
    },
    emitDeselect() {
      this.$emit('deselect', this.data.id);
    },
  },
};
</script>

<style lang="scss" scoped></style>
