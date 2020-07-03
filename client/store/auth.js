export const state = () => ({
  access: '',
  refresh: '',
  user: {},
})

export const getters = {
  loggedIn: (state) => !!state.access,
}

export const mutations = {
  setAccess(state, payload) {
    state.access = payload
  },
  setRefresh(state, payload) {
    state.refresh = payload
  },
  setUser(state, payload) {
    state.user = payload
  },
  clearTokens(state) {
    state.access = ''
    state.refresh = ''
  },
}

export const actions = {
  async processLoggedInData({ commit }, payload) {
    try {
      this.$axios.setHeader('Authorization', `Bearer ${payload.access}`)
      commit('setAccess', payload.access)
      commit('setRefresh', payload.refresh)
      const user = await this.$axios.$get('users/auth/me/')
      commit('setUser', user)
      return Promise.resolve()
    } catch (err) {
      return Promise.reject(err)
    }
  },
}
