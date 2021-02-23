<template>
  <ul class="social flex">
    <li v-for="item in items" class="mr-2">
      <a :href="item.url" v-html="item.icon"></a>
    </li>
  </ul>
</template>
<script>
export default {
  data() {
    return {
      items:[
        {
          url: '/',
          icon: '<svg width="37" height="37" viewBox="0 0 37 37" fill="none" xmlns="http://www.w3.org/2000/svg">\n' +
            '<ellipse cx="18.8434" cy="18.1191" rx="17.986" ry="18" fill="#F6F6F6"/>\n' +
            '<path d="M20.2496 27.1163V18.9203H23.0146L23.4256 15.7113H20.2496V13.6673C20.2496 12.7413 20.5076 12.1073 21.8366 12.1073H23.5206V9.24631C22.7012 9.1585 21.8776 9.1161 21.0536 9.11931C18.6096 9.11931 16.9316 10.6113 16.9316 13.3503V15.7053H14.1846V18.9143H16.9376V27.1163H20.2496Z" fill="#2B4724"/>\n' +
            '</svg>'
        },
        {
          url: '/',
          icon: '<svg width="37" height="37" viewBox="0 0 37 37" fill="none" xmlns="http://www.w3.org/2000/svg">\n' +
            '<ellipse cx="18.8151" cy="18.1191" rx="17.986" ry="18" fill="#F6F6F6"/>\n' +
            '<path d="M26.4898 9.83498L8.7598 16.672C7.5498 17.158 7.5568 17.833 8.5378 18.134L13.0898 19.554L23.6218 12.909C24.1198 12.606 24.5748 12.769 24.2008 13.101L15.6678 20.802H15.6658L15.6678 20.803L15.3538 25.495C15.8138 25.495 16.0168 25.284 16.2748 25.035L18.4858 22.885L23.0848 26.282C23.9328 26.749 24.5418 26.509 24.7528 25.497L27.7718 11.269C28.0808 10.03 27.2988 9.46898 26.4898 9.83498Z" fill="#2B4724"/>\n' +
            '</svg>'
        },
      ],
    };
  },
}
</script>
<style scoped lang="scss">
@import "assets/scss/abstracts/variables";
  .social {

  }
</style>
