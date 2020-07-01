export const state = () => ({
  snackbar: false,
  snackbarMessage: '',
  snackbarColor: 'error',
  snackbarTimeout: 7500,
})

export const mutations = {
  setSnackbarData(state, payload) {
    state.snackbar = payload.snackbar || false
    state.snackbarMessage = payload.message || ''
    state.snackbarColor = payload.color || 'error'
    state.snackbarTimeout = payload.timeout || 7500
  },
}

export const getters = {
  getSnackbarData: (state) => ({
    snackbar: state.snackbar,
    message: state.snackbarMessage,
    color: state.snackbarColor,
    timeout: state.snackbarTimeout,
  }),
}
