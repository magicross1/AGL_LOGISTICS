// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app:{
    baseURL: '/agl/', // 部署在子目录时使用
    head: {
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/agl/agl-favicon.ico' }
      ]
    }
  },
  
  devServer: {
    port: 8081
  },
  
  modules: [
    '@nuxt/eslint',
    '@nuxt/image',
    '@nuxt/ui',
    '@nuxt/content'
  ],

  devtools: {
    enabled: true
  },

  css: ['~/assets/css/main.css'],

  mdc: {
    highlight: {
      noApiRoute: false
    }
  },

  compatibilityDate: '2025-01-15',

  // Enhanced Prerendering
  nitro: {
    prerender: {
      routes: [
        '/',
        '/about',
        '/contact',
        '/careers',
        '/services/air-freight',
        '/services/sea-freight',
        '/services/special-transports',
        '/services/customs-brokerage',
        '/services/storage',
        '/service-center',
        '/service-center/news',
        '/service-center/notices',
        '/service-center/downloads',
        '/offices/sydney',
        '/offices/melbourne',
        '/offices/brisbane',
        '/offices/perth'
      ]
    }
  },

  eslint: {
    config: {
      stylistic: {
        commaDangle: 'never',
        braceStyle: '1tbs'
      }
    }
  }
})