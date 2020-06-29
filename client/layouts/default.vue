<template>
  <v-app>
    <v-main>
      <v-app-bar id="app-bar" app flat>
        <nuxt-link exact to="/">Home</nuxt-link>
        <v-spacer />
        <BaseMenu />
      </v-app-bar>
      <v-container fluid>
        <v-btn @click="test">Try authorized Route</v-btn>
        <v-btn @click="toggleSnackbar">Toggle Snackbar</v-btn>
        <nuxt />
      </v-container>
    </v-main>
    <TheSnackbar />
    <v-footer fixed app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
import TheSnackbar from '@/components/functional-components/TheSnackbar'

export default {
  components: {
    BaseMenu: () => import('@/layouts/nav-menus/BaseMenu'),
    TheSnackbar,
  },
  methods: {
    toggleSnackbar() {
      this.$store.commit('setSnackbarData', {
        message: 'test message',
        color: 'purple',
        snackbar: true,
        snackbarTimeout: 2500,
      })
    },
    test() {
      this.$axios.$get('/auth/users/me/')
    },
  },
}
</script>

<style></style>
