<template>
  <div class="not-found">
    <div class="container mt-3">
      <h1 id="notfound">{{ message }}</h1>
    </div>
  </div>
</template>

<script scoped>
export default {
  name: "NotFound",
  data() {
    return {
      message: "For hundred and Four - Page not FOund",
    };
  },
};
</script>

<style>
#notfound {
  color: red;
  text-align: center;
}
</style>