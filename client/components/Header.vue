<template>
  <div class="pt-4">
    <div class="shadow-md sm:shadow-sm w-full header p-3">
      <div class="sm:container sm:mx-auto grid grid-cols-12 gap-5 items-center">
      <div class="col-span-2 sm:col-span-3"><NuxtLink to="/">
        <img src="/image/logo.svg" alt=""></NuxtLink></div>
      <div class="col-span-8 text-xs sm:text-xl sm:col-span-6 sm:text-center">Правовые консультации по делам связанным с наркотиками</div>
      <div class="col-span-2 sm:col-span-3 text-right">
        <IconifyIcon class="sm:hidden text-4xl " @click="nav = true" :icon="icons.menuIcon" />
        <NuxtLink to="/search"><IconifyIcon class="hidden sm:inline text-3xl mr-3" @click="nav = true" :icon="icons.searchOutlined" /></NuxtLink>
        <NuxtLink to="/" class="btn-accent hidden sm:inline">Поддержать</NuxtLink>
      </div>
      <nav class="mobile-nav p-10" v-show="nav">
        <div class="flex justify-between align-center">
          <FormSearch class="w-10/12	"></FormSearch>
            <IconifyIcon @click="nav = false" class="sm:hidden text-4xl " :icon="icons.closeOutline" />
        </div>
        <ul class="menu nav py-3">
          <li class="font-medium font-secondary py-1" v-for="item in menu">
            <span  v-if="!item.childs" @click="nav = false">
              <NuxtLink :to="item.slug" class="text-lg">{{ item.name }}</NuxtLink>
            </span>
            <span v-else @click=""  class="text-lg font-medium mr-2 lg:mr-10 cursor-pointer">
            {{item.name}}
            <IconifyIcon style="display: inline" v-bind:class="{'open': openChild === item.index}" :icon="icons.arrowDown"  />
          </span>
            <ul v-if="item.childs && item.index === openChild" class="pl-5 py-4">
              <li v-for="child in item.childs" ><NuxtLink class="text-lg block py-3" :to="child.slug" >{{child.name}}</NuxtLink></li>
            </ul>
          </li>

        </ul>
        <div class="text-center pt-3">
          <NuxtLink to="/" class="btn-accent" @click="nav = false">Поддержать</NuxtLink>
        </div>
      </nav>
      </div>
      <div class="menu container mx-auto mt-5 hidden sm:block">
        <ul class="flex justify-center">
        <li v-for="(item, index) in menuDesc" :key="index" class="relative">
          <NuxtLink v-if="!item.childs" :to="item.slug" class="text-xl font-medium mr-2 lg:mr-10 cursor-pointer">{{item.name}}</NuxtLink>
          <span v-else @click="(openChild === item.index)?openChild ='': openChild = item.index"  class="text-xl font-medium mr-2 lg:mr-10 cursor-pointer">
            {{item.name}}
            <IconifyIcon style="display: inline" v-bind:class="{'open': openChild === item.index}" :icon="icons.arrowDown"  />
          </span>
          <ul v-if="item.childs && item.index === openChild" class="bg-white shadow-md p-5 absolute top-1	">
            <li v-for="child in item.childs"><NuxtLink class="text-xl block py-3 font-medium" :to="child.slug">{{child.name}}</NuxtLink></li>
          </ul>
        </li>
      </ul>
      </div>
    </div>
    <div class="place"></div>
  </div>
</template>
<script>
import IconifyIcon from '@iconify/vue';
import menuIcon from '@iconify/icons-heroicons-solid/menu';
import closeOutline from '@iconify/icons-ion/close-outline';
import searchOutlined from '@iconify/icons-ant-design/search-outlined';
import arrowDown from '@iconify/icons-fe/arrow-down';

export default {
  components: {
    IconifyIcon,
  },
  data() {
    return {
      icons: {
        menuIcon,
        closeOutline,
        searchOutlined,
        arrowDown
      },
      childOpen: '',
      menuDesc:[
        {
          slug: '/',
          name: 'Консультации'
        },
        {
          slug: '/',
          name: 'Блоги'
        },
        {
          slug: '/',
          name: 'База знаний',
          childs: [
            {
              slug: '/',
              name: 'Памятки'
            },
            {
              slug: '/',
              name: 'Образцы документов'
            },
            {
              slug: '/',
              name: 'Судебная практика'
            },
            {
              slug: '/',
              name: 'Законодательство'
            },
            {
              slug: '/',
              name: 'Библиотека'
            }
          ]
        },
        {
          slug: '/',
          name: 'Разборы'
        },
        {
          slug: '/',
          name: 'Все теги'
        },
        {
          slug: '/',
          name: 'О нас'
        },
      ],
      menu: [
        {
          slug: '/',
          name: 'Консультации'
        },
        {
          slug: '/',
          name: 'Блоги',
          childs: [
            {
              slug: '/',
              name: 'Колонка руководителя'
            },
            {
              slug: '/',
              name: 'Трибуна консультантов'
            },
            {
              slug: '/',
              name: 'Дискуссионные вопросы уголовного судопроизводства'
            },
          ]
        },
        {
          slug: '/',
          name: 'Памятки'
        },
        {
          slug: '/',
          name: 'Образцы документов'
        },
        {
          slug: '/',
          name: 'Судебная практика'
        },
        {
          slug: '/',
          name: 'Законодательство'
        },
        {
          slug: '/',
          name: 'Темы'
        },
        {
          slug: '/',
          name: 'Новости сайта'
        },
        {
          slug: '/',
          name: 'О нас'
        },
        {
          slug: '/',
          name: 'Все теги'
        },
      ],
      nav: false
    };
  },
  methods: {
    openChild(item){
      (this.childOpen === item.index)?this.childOpen ='': this.childOpen = item.index
    }
  }
}
</script>
<style scoped lang="scss">
@import "assets/scss/abstracts/variables";
  .place{
    padding-top: 63px;

    @media (min-width: 640px) {
      padding-top: 150px;
    }
  }
  .header{
    background-color: white;
    border-bottom: 1px solid $color-gray-20;
    position: fixed;
    left: 0;
    right: 0;
    width: 100%;
    top: 0;
    .title{
      font-size: 10px;
    }

    .menu {
      .open {
        transform: rotate(180deg);
      }
    }

    .mobile-nav{
      position: fixed;
      bottom: 0;
      top: 0;
      right: 0;
      left: 0;
      background-color: white;
    }
  }
</style>
