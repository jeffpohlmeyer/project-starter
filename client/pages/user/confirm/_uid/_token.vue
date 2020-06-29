<template>
  <v-row v-if="!error" justify="center" no-gutters>
    <v-col cols="4">
      <p class="display-4">
        Success
      </p>
      <p class="display-1">
        You have confirmed your email address and activated your account. Click
        <nuxt-link to="/user/log-in">here</nuxt-link> to log in.
      </p>
    </v-col>
  </v-row>
  <div v-else>Please wait</div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  data: () => ({
    error: true,
    loading: false,
  }),
  async mounted() {
    try {
      await this.$axios.$post('auth/users/activation/', {
        uid: this.$route.params.uid,
        token: this.$route.params.token,
      })
      this.error = false
    } catch (err) {
      let message
      try {
        message = err.response.data.error
      } catch {
        message = 'There was an unidentified error.  Please try again later.'
      }
      this.setSnackbarData({
        snackbar: true,
        message,
      })
      await this.$router.push(`/user/re-generate/confirm/${this.email}`)
    }
  },
  methods: {
    ...mapMutations({
      setSnackbarData: 'setSnackbarData',
    }),
  },
}
</script>

<style scoped lang="scss"></style>
