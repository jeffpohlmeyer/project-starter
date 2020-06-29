export default function ({ $axios, $auth, store }) {
  // $axios.onRequest((config) => {
  //   console.log('Making request to ' + config.url)
  // })

  // https://cmty.app/nuxt/axios-module/issues/c230
  $axios.onError(async (error) => {
    const code = parseInt(error.response && error.response.status)
    if (code === 401 && store.state.auth.loggedIn) {
      if (error.response.config.url.includes('/jwt/refresh/')) {
        await $auth.logout()
        throw error
      } else {
        try {
          const response = await $axios.$post('/auth/jwt/refresh/', {
            refresh: store.state.refresh,
          })
          $axios.setHeader('Authorization', `Bearer ${response.access}`)
          await $auth.setToken('customStrategy', response.access)
          return $axios.$request({
            method: error.response.config.method,
            url: error.response.config.url,
            data: error.response.config.data,
          })
        } catch {
          throw error
        }
      }
    } else {
      throw error
    }
  })
}
