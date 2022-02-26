<template>
  <div class="container">
    <h1>ImGames 2.0 - платформа для геймификации</h1>
    <router-link :to="'/auth'">AUTH</router-link>
  </div>
</template>

<script>
export default {
  name: 'FirstComponent',
};
</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
</style>
