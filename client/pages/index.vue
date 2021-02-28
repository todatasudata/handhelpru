<template>
  <div class="sm:grid sm:grid-cols-9 gap-10 container mx-auto">
    <div class="sm:col-span-5 py-10 sm:py-20 px-3 sm:px-0">
      <div class="sm:grid sm:grid-cols-2 pb-8 sm:pb-20">
        <div class="text-md sm:text-lg sm:col-span-2" v-html="page.text"></div>
        <div class="text-xs sm:text-lg sm:col-start-2 pl-4 sm:pl-0 pt-3 sm:pt-10" v-html="page.text_sign"></div>
      </div>
      <div class="sm:hidden py-10 text-center">
        <NuxtLink class="btn-secondary" to="/">Перейти к консультациям</NuxtLink>
      </div>
      <ul class="mt-4">
        <li class="p-5 sm:px-8 sm:py-10 mb-4 rounded-md bg-gray-20 text-lg sm:text-2xl font-medium" v-for="item in page.ads" v-html="item.value">
        </li>
      </ul>
      <h2 class="text-2xl sm:text-3xl font-secondary text-center py-8 sm:py-16">Новости сайта</h2>
      <ul class="pb-3">
        <li v-for="item in news.content" class="border-b py-3">
          <div class="text-md sm:text-lg pb-3 text-gray-60">{{item.value.date}}</div>
          <div class="text-md sm:text-lg" v-html="item.value.text"></div>
        </li>
      </ul>
      <div  class="text-center pt-4 sm:pt-8"><NuxtLink to="/" class="btn-outline-gray--lg inline-block">Все новости</NuxtLink></div>
    </div>
    <div class="sm:col-span-4 sm:py-20 px-3 sm:px-0">
      <img class="w-full sm:mb-20 hidden sm:block" :src="server + page.image.url" alt="">
      <div class="pt-5 sm:pt-0 pb-5 sm:pb-10">
        <h2 class="text-2xl sm:text-3xl font-secondary text-center">Колонка руководителя</h2>
        <p class="text-center text-xl sm:text-2xl font-secondary">Новости и комментарии</p>
      </div>
      <ul class="">
        <li v-for="item in blog.items" class="my-3 rounded-lg overflow-hidden	">
          <div class="bg-secondary py-3 px-3 sm:px-8 text-right text-white text-md sm:text-lg">Блоги</div>
          <div class="py-3 px-3 sm:px-8 bg-gray-20">
            <div class="flex pb-8">
              <span class="text-md sm:text-lg">Теги:</span>
              <ul class="inline"><li v-for="tag in item.tags"><NuxtLink to="/"  class="text-md sm:text-lg text-secondary ml-1">{{tag.name}}</NuxtLink></li></ul>
            </div>
            <div  class="text-md sm:text-lg" v-for="author in item.blog_authors">{{author.author_name}}</div>
            <div class="text-lg sm:text-xl font-medium border-b pb-3">{{ item.title }}</div>
            <div class="text-md sm:text-lg pt-3 ">{{item.publish_date}}</div>
          </div>
        </li>
      </ul>
      <div class="text-center  pt-5 sm:pt-8"><NuxtLink to="/" class="btn-outline-gray--lg inline-block">Все новости</NuxtLink></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      server: process.env.SERVER_URL
    };
  },
async asyncData({ $axios }) {
  const page = await $axios.$get('/api/v2/pages/4/')
  const news = await $axios.$get('/api/v2/pages/10')
  const blog = await $axios.$get('/api/v2/pages/?type=blog.BlogArticlePage&child_of=11&order=-publish_date&limit=5&fields=*')
  return {page,news,blog}
}
}
</script>

<style>
</style>
