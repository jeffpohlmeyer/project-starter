<template>
  <v-form v-if="error" ref="form" v-model="valid">
    <BaseUserComponent>
      <EmailTextField
        v-model="email"
        autofocus
        @enterPressed="reGenerateEmail"
      />
      <template v-slot:title>
        Re-Send Activation Email
      </template>
      <template v-slot:proceed>
        <base-button :loading="loading" block @click="reGenerateEmail">
          Send Email
        </base-button>
      </template>
    </BaseUserComponent>
  </v-form>
  <div v-else>Please wait</div>
</template>

<script>
import { mapMutations, mapActions } from 'vuex'
import useErrorParser from '~/utils/parse-errors'
import BaseUserComponent from '~/components/user/BaseUserComponent'
import EmailTextField from '~/components/functional-components/EmailTextField'

export default {
  components: {
    BaseUserComponent,
    EmailTextField,
  },
  data: () => ({
    email: '',
    valid: true,
    error: false,
    loading: false,
  }),
  async mounted() {
    try {
      const response = await this.$axios.$post('users/auth/activation/', {
        uid: this.$route.params.uid,
        token: this.$route.params.token,
      })
      await this.processLoggedInData(response)
      this.error = false
    } catch (err) {
      let message = ''
      try {
        message = useErrorParser(err.response)
      } catch {
        message =
          'There was a problem with the activation link.  Please create another.'
      }
      this.setSnackbarData({
        snackbar: true,
        message,
      })
      this.error = true
    }
  },
  methods: {
    ...mapMutations({
      setSnackbarData: 'setSnackbarData',
    }),
    ...mapActions({
      processLoggedInData: 'auth/processLoggedInData',
    }),
    async reGenerateEmail() {
      if (this.$refs.form.validate()) {
        this.loading = true
        try {
          await this.$axios.$post('users/auth/resend_activation/', {
            email: this.email,
          })
          await this.$router.push('/user/notify')
        } catch (err) {
          let message = ''
          const snackbar = true
          try {
            message = useErrorParser(err.response.data)
          } catch {
            message =
              'There was an unidentified error.  Please try again later.'
          }
          this.setSnackbarData({
            snackbar,
            message,
          })
        } finally {
          this.loading = false
        }
      }
    },
  },
}
</script>

<style scoped lang="scss"></style>
