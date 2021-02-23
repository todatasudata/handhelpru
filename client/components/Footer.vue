<template>
  <div class="footer mt-16 sm:border-t">
    <div class="sm:container sm:mx-auto p-3">
      <div class="sm:grid grid-cols-2 gap-x-40 gap-4 w-full">
      <div class="sm:col-span-1 pt-5">
        <ul>
          <li v-for="item in menu" class="text-md sm:text-lg text-white   sm:py-3 ">
            <NuxtLink to="item.url">
              {{item.name}}
            </NuxtLink>
          </li>
          <li class="text-md text-white py-1  sm:py-3  sm:text-lg"><a href="mailto:hand-help-lev@yandex.ru">Email: hand-help-lev@yandex.ru</a></li>
        </ul>
        <Social class="mt-3"></Social>
        </div>
        <hr class="sm:hidden mt-5 border-gray-500">
        <div class="sm:col-span-1">
          <Subscribe class="pt-8"></Subscribe>
          <Mistaker class="pt-10"></Mistaker>
        </div>
        <div class="pt-5">
          <div class="text-lg sm:text-xl text-white sm:col-span-1 py-2">
            АНО Институт прав человека
            2007 — 2021
          </div>
          <div class="text-white sm:col-span-1 py-2">
            По решению Минюста РФ 20 ноября 2015 года Институт прав человека включен в реестр некоммерческих организаций, выполняющих функции иностранного агента.
          </div>
        </div>

      <div class="sm:col-span-1 sm:block pt-5">
        <div>
          <img class="w-30 sm:w-40" src="/license.png" alt="Лицензия CC0 1.0 Универсальная">
        </div>
        <div class="pt-5 text-white sm:text-xl">
          Все материалы на сайте переданы в общественное достояние. <a class="underline" href="">Лицензия CC0 1.0 Универсальная</a>
        </div>
      </div>
        <div class="py-3 text-white sm:col-span-1 flex sm:block">
         Разработка и поддержка <a class="pl-1 underline" href="https://itcoop.ru/">It-coop</a>
      </div>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  data() {
    return {
      menu: [
        {
          slug: '/',
          name: 'Задать вопрос'
        },
        {
          slug: '/',
          name: 'Особые темы'
        },
        {
          slug: '/',
          name: 'Институт прав человека'
        },
        {
          slug: '/',
          name: 'Поддержать проект'
        },
        {
          slug: '/',
          name: 'Новости сайта'
        },
      ],
    };
  },

}
</script>
<style scoped lang="scss">
@import "assets/scss/abstracts/variables";
.footer{
  background-color: black;

  @media (min-width: 640px) {
    background-color: black;
  }
}

</style>
