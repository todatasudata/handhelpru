export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'client',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '~/assets/scss/main.scss'
  ],
  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/tailwindcss
    '@nuxtjs/tailwindcss',
    '@nuxtjs/google-analytics',
    '@aceforth/nuxt-optimized-images',
    '@nuxtjs/google-fonts',

  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    '@nuxtjs/robots',
    '@nuxtjs/redirect-module',
    '@nuxtjs/yandex-metrika',
    '@nuxtjs/sitemap',
      [
      "nuxt-social-meta",
      {
        url: "Site url",
        title: "Title",
        site_name: "Site name",
        description: "Site description",
        img: "Link to image in static folder",
        locale: "en_US",
        twitter: "@user",
        twitter_card: "summary_large_image",
        themeColor: "#theme-color",
      },
    ],
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // baseURL: process.env.SERVER_URL, // Used as fallback if no runtime config is provided
    proxy: true // Can be also an object with default options
  },
  yandexMetrika: {
    id: 'XXXXXX',
    // ...
  },
  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en'
    }
  },
  googleAnalytics: {
    id: 'UA-XXX-X'
  },
  robots: {
    /* module options */
  },
  redirect: [
    // Redirect options here
  ],
  optimizedImages: {
    inlineImageLimit: 1000,
    imagesName: ({ isDev }) => isDev ? '[path][name][hash:optimized].[ext]' : 'img/[contenthash:7].[ext]',
    responsiveImagesName: ({ isDev }) => isDev ? '[path][name]--[width][hash:optimized].[ext]' : 'img/[contenthash:7]-[width].[ext]',
    handleImages: ['jpeg', 'png', 'svg', 'webp', 'gif'],
    optimizeImages: true,
    optimizeImagesInDev: true,
    defaultImageLoader: 'img-loader',
    mozjpeg: {
      quality: 80,
    },
    optipng: {
      optimizationLevel: 3,
    },
    pngquant: false,
    gifsicle: {
      interlaced: true,
      optimizationLevel: 3,
    },
    svgo: {
      // enable/disable svgo plugins here
    },
    webp: {
      preset: 'default',
      quality: 75,
    },
  },
  sitemap: {
    hostname: 'https://example.com',
    lastmod: '2017-06-30',
    sitemaps: [
      {
        path: '/sitemap-foo.xml',
        routes: ['foo/1', 'foo/2'],
        gzip: true
      }, {
        path: '/folder/sitemap-bar.xml',
        routes: ['bar/1', 'bar/2'],
        exclude: ['/**']
      }
    ]
  },
  googleFonts: {
    families: {
      Montserrat: {
        wght: [300, 500],
      },
      Raleway: {
        wght: [500],
      },
    }
  },
  proxy: {
    '/api/': process.env.SERVER_URL,
  },
  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
