<template>
  <div class="subscribe">
    <div class="text-white text-lg">Наша рассылка</div>
    <div class="pt-3"><input class="rounded" type="text" placeholder="Введите Email"></div>
    <div class="pt-3">
    <span class="inline-block btn-accent">Подписаться</span>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
    };
  },
}
</script>
<style scoped lang="scss">
@import "assets/scss/abstracts/variables";
  .subscribe {
    input{
      background-color: $color-gray-20;
      display: block;
      font-size: $type-large;
      padding: 15px 15px;
      line-height: 1.5;
      font-family: $font-primary;
      font-weight: 400;
      width: 100%;

      @media (min-width: 640px) {
        width: auto;
        min-width: 400px;
      }

      &::placeholder{
        font-weight: 400 !important;
        font-family: $font-primary !important;
      }
    }
  }
</style>
