<template>
  <ForgotComponent
    :loading="loading"
    @triggerForgotEvent="triggerForgotEvent"
  />
</template>

<script>
import { mapMutations } from 'vuex'
import useErrorParser from '~/utils/parse-errors'
import ForgotComponent from '~/components/user/ForgotComponent'

export default {
  components: {
    ForgotComponent,
  },
  data: () => ({
    email: '',
    valid: true,
    loading: false,
  }),
  methods: {
    ...mapMutations({
      setSnackbarData: 'setSnackbarData',
    }),
    async triggerForgotEvent(email) {
      this.loading = true
      try {
        await this.$axios.$post('users/auth/reset_username/', {
          email,
        })
        await this.$router.push('notify/reset')
      } catch (err) {
        let message = ''
        const snackbar = true
        try {
          message = useErrorParser(err.response.data)
        } catch {
          message = 'There was an unidentified error.  Please try again later.'
        }
        this.setSnackbarData({
          snackbar,
          message,
        })
      } finally {
        this.loading = false
      }
    },
  },
}
</script>

<style scoped lang="scss"></style>
