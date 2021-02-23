<template>
  <div class="base">
    <Header></Header>
    <Nuxt/>
    <Footer class="self-end"></Footer>
  </div>
</template>
<style scoped lang="scss">
@import "assets/scss/abstracts/variables";
.base {
  font-family: $font-primary;
  font-size: 14px;
  font-weight: lighter;
}
</style>
