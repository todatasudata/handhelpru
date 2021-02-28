<template>
  <div class="subscribe">
    <div class="text-white text-md sm:text-lg">Наша рассылка</div>
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
      font-size: $type-base;
      line-height: 1.5;
      font-family: $font-primary;
      font-weight: 300;
      width: 100%;
      padding: 10px 10px;

      &::placeholder{
        font-size: $type-base;
        color: $color-gray-60;
        font-weight: 300;
      }

      @media (min-width: 640px) {
        width: auto;
        min-width: 400px;
        padding: 15px 15px;
        font-size: $type-large;

        &::placeholder{
          font-size: $type-large;
        }
      }

      &::placeholder{
        font-weight: 400 !important;
        font-family: $font-primary !important;
      }
    }
  }
</style>
