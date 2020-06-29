<template>
  <v-form ref="form" v-model="valid">
    <BaseUserComponent>
      <v-row justify="space-between" no-gutters>
        <v-col cols="12">
          <UsernameTextField
            v-model="username"
            autofocus
            @enterPressed="signup"
          />
        </v-col>
        <v-col cols="12">
          <EmailTextField v-model="email" @enterPressed="signup" />
        </v-col>
        <v-col cols="12">
          <PasswordTextField v-model="password" @enterPressed="signup" />
        </v-col>
        <v-col cols="12">
          <PasswordTextField
            v-model="password2"
            :password-compare="password"
            label="Confirm Password"
            @enterPressed="signup"
          />
        </v-col>
      </v-row>
      <template v-slot:title>
        Sign Up
      </template>
      <template v-slot:proceed>
        <base-button :loading="loading" block @click="signup">
          Sign Up
        </base-button>
      </template>
      <template v-slot:alternateNavigation>
        Already have an account? Click
        <nuxt-link to="log-in">here</nuxt-link> to log in.
      </template>
    </BaseUserComponent>
  </v-form>
</template>

<script>
import { mapMutations } from 'vuex'

import PasswordTextField from '~/components/functional-components/PasswordTextField.vue'
import UsernameTextField from '~/components/functional-components/UsernameTextField'
import EmailTextField from '~/components/functional-components/EmailTextField'

export default {
  components: {
    EmailTextField,
    PasswordTextField,
    UsernameTextField,
    BaseUserComponent: () => import('~/components/user/BaseUserComponent.vue'),
  },
  data: () => ({
    username: '',
    email: '',
    password: '',
    password2: '',
    loading: false,
    valid: true,
  }),
  methods: {
    ...mapMutations({
      setSnackbarData: 'setSnackbarData',
    }),
    async signup() {
      if (this.$refs.form.validate()) {
        this.loading = true
        try {
          await this.$axios.$post('auth/users/', {
            username: this.username,
            email: this.email,
            password: this.password,
            re_password: this.password2,
          })
          await this.$router.push('notify')
        } catch (err) {
          let message
          const snackbar = true
          try {
            message = err.response.data.error
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
