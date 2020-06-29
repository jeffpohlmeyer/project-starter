<template>
  <v-form ref="form" v-model="valid">
    <BaseUserComponent>
      <v-row justify="space-between" no-gutters>
        <v-col cols="12">
          <PasswordTextField
            v-model="password"
            autofocus
            @enterPressed="updatePassword"
          />
        </v-col>
        <v-col cols="12">
          <PasswordTextField
            v-model="password2"
            :password-compare="password"
            label="Confirm Password"
            @enterPressed="updatePassword"
          />
        </v-col>
      </v-row>
      <template v-slot:title>Reset password for {{ email }}.</template>
      <template v-slot:proceed>
        <base-button :loading="loading" block @click="updatePassword">
          Update Password
        </base-button>
      </template>
    </BaseUserComponent>
  </v-form>
</template>

<script>
import { mapMutations } from 'vuex'
import PasswordTextField from '@/components/functional-components/PasswordTextField'
export default {
  components: {
    PasswordTextField,
    BaseUserComponent: () => import('~/components/user/BaseUserComponent.vue'),
  },
  fetch(context) {
    // eslint-disable-next-line
    console.log('context', context)
  },
  data: () => ({
    valid: true,
    password: '',
    password2: '',
    loading: false,
    error: false,
  }),
  computed: {
    email() {
      return this.$route.params.email
    },
    isLoggedIn() {
      return this.$auth.loggedIn
    },
  },
  methods: {
    ...mapMutations({
      setSnackbarData: 'setSnackbarData',
    }),
    async updatePassword() {
      this.loading = true
      try {
        const response = await this.$axios.$post(
          'user/change-password-from-forgot',
          {
            email: this.email,
            password: this.password,
            token: this.$route.params.token,
          }
        )
        await this.$auth.setUserToken(response.token)
        await this.$router.push('/user')
      } catch (err) {
        let message
        const snackbar = true
        try {
          message = err.response.data.error
        } catch {
          message = 'There was an unidentified error.  Please try again later.'
        }
        this.setSnackbarData({
          snackbar,
          message,
        })
        if (!!err.response && err.response.status === 409) {
          await this.$router.push(`/user/re-generate/password/${this.email}`)
        }
      } finally {
        this.loading = false
      }
    },
  },
}
</script>

<style scoped lang="scss"></style>
