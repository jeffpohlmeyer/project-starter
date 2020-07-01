export const state = () => ({
  access: '',
  refresh: '',
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
  clearTokens(state) {
    state.access = ''
    state.refresh = ''
  },
}
