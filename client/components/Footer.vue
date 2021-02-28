<template>
  <div class="footer mt-16 sm:border-t">
    <div class="md:container sm:mx-auto p-3">
      <div class="md:grid grid-cols-2 gap-x-40 gap-4 w-full">
      <div class="md:col-span-1 pt-5">
        <ul>
          <li v-for="item in menu" class="text-md sm:text-lg text-white font-medium py-2 sm:py-3 ">
            <NuxtLink to="item.url">
              {{item.name}}
            </NuxtLink>
          </li>
        </ul>
        <Mistaker class="pt-10"></Mistaker>
        </div>
        <hr class="sm:hidden mt-5 border-gray-500">
        <div class="md:col-span-1">
          <Subscribe class="pt-8"></Subscribe>
          <div class="hidden sm-block text-lg">Контакты</div>
          <div class="text-md text-gray-20 pt-8  sm:text-lg"><a href="mailto:hand-help-lev@yandex.ru">Email: hand-help-lev@yandex.ru</a></div>
          <Social class="mt-3"></Social>
        </div>
        <div class="pt-8">
          <div class="text-md sm:text-xl text-gray-20 sm:col-span-1 py-2">
            АНО Институт прав человека
            2007 — 2021
          </div>
          <div class="text-xs sm:text-md text-gray-20 sm:col-span-1 py-2">
            По решению Минюста РФ 20 ноября 2015 года Институт прав человека включен в реестр некоммерческих организаций, выполняющих функции иностранного агента. «Любые попытки обнаружить в словосочетании "иностранный агент" ... отрицательные контексты лишены каких-либо конституционно-правовых оснований»  (Постановление Конституционного Суда РФ от 8 апреля 2014 г. № 10-П.)</div>
        </div>

      <div class="md:col-span-1 sm:block pt-5">
        <div>
          <img class="w-20 sm:w-40" src="/license.png" alt="Лицензия CC0 1.0 Универсальная">
        </div>
        <div class="pt-5 text-gray-20 sm:text-xl">
          Все материалы на сайте переданы в общественное достояние. <a class="underline" href="">Лицензия CC0 1.0 Универсальная</a>
        </div>
      </div>
        <div class="py-3 text-gray-20 sm:col-span-1 flex sm:block">
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
