import createPersistedState from 'vuex-persistedstate'
import * as Cookies from 'js-cookie'

export default ({ store }) => {
  createPersistedState({
    paths: 'refresh',
    storage: {
      getItem: (key) => Cookies.get(key),
      setItem: (key, value) =>
        Cookies.set(key, value, { expires: 7, secure: false }),
      removeItem: (key) => Cookies.remove(key),
    },
  })(store)
}
