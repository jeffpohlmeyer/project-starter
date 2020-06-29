<template>
  <v-snackbar
    v-model="snackbar"
    :color="getSnackbarData.color"
    :timeout="getSnackbarData.timeout"
  >
    {{ getSnackbarData.message }}
    <base-button color="white" text @click="snackbar = false">
      Close
    </base-button>
  </v-snackbar>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'
export default {
  name: 'TheSnackbar',
  computed: {
    ...mapGetters(['getSnackbarData']),
    snackbar: {
      get() {
        return this.getSnackbarData.snackbar
      },
      set(value) {
        this.setSnackbarData({ snackbar: value })
      },
    },
  },
  methods: {
    ...mapMutations({
      setSnackbarData: 'setSnackbarData',
    }),
  },
}
</script>

<style scoped></style>
