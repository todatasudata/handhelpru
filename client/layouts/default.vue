<template>
  <div class="base">
    <Header></Header>
    <Nuxt/>
    <Footer class="self-end"></Footer>
  </div>
</template>
<script>
export default {
  data() {
    return {
      topScroll: false
    };
  },
  methods: {
    handleScroll (event) {
      this.topScroll = (event.deltaY < 0)
      this.$nuxt.$emit('topScroll', this.topScroll)
    }
  },
  created () {
    if (process.browser) {
      window.addEventListener('wheel', this.handleScroll);
    }
  },
  destroyed () {
    if (process.browser) {
      window.removeEventListener('wheel', this.handleScroll);
    }
  }
}
</script>
<style scoped lang="scss">
@import "assets/scss/abstracts/variables";
.base {
  font-family: $font-primary;
  font-size: 14px;
  font-weight: lighter;
}
</style>
