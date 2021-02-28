<template>
  <div class="from-search">
    <input type="search" class="rounded" placeholder="Введите запрос">
    <IconifyIcon class="icon text-xl" :icon="icons.searchOutlined" />
  </div>
</template>
<script>
import IconifyIcon from '@iconify/vue';
import searchOutlined from '@iconify/icons-ant-design/search-outlined';

export default {
  components: {
    IconifyIcon,
  },
  data() {
    return {
      icons: {
        searchOutlined,
      },
    };
  },
}
</script>
<style scoped lang="scss">
@import "assets/scss/abstracts/variables";
  .from-search{
    position: relative;
    align-items: center;
    display: flex;

    input{
      background-color: $color-gray-20;
      display: block;
      font-size: $type-large;
      padding: 5px 15px;
      line-height: 1.5;
      width: 100%;
      padding-left: 35px;

      &::placeholder{
        color: $color-gray-60;
        font-weight: 300;
        font-size: $type-base;
      }
    }

    .icon{
      position: absolute;
      left: 5px;
      top: 9px;
    }
  }
</style>
