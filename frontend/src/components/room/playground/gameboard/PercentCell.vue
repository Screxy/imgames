<template>
  <td>{{ value }}%</td>
</template>

<script>
export default {
  name: 'PercentCell',
  props: {
    value: {
      type: Number,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped></style>
