<template>
  <v-form ref="form" v-model="valid">
    <BaseUserComponent>
      <v-row justify="space-between" no-gutters>
        <v-col cols="12">
          <UsernameTextField
            v-model="username"
            autofocus
            :error="usernameError"
            :error-messages="usernameErrorMessages"
            @enterPressed="signup"
            @blur="checkUsername"
          />
        </v-col>
        <v-col cols="12">
          <EmailTextField
            v-model="email"
            :error="emailError"
            :error-messages="emailErrorMessages"
            @enterPressed="signup"
            @blur="checkEmail"
          />
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
import useErrorParser from '~/utils/parse-errors'

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
    usernameError: false,
    usernameErrorMessages: '',
    email: '',
    emailError: false,
    emailErrorMessages: '',
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
          await this.$axios.$post('users/auth/', {
            username: this.username,
            email: this.email,
            password: this.password,
            re_password: this.password2,
          })
          await this.$router.push('notify')
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
    async checkUsername() {
      try {
        await this.$axios.get(
          `users/check_availability/?username=${this.username}`
        )
        this.usernameErrorMessages = ''
        this.usernameError = false
      } catch (err) {
        this.usernameErrorMessages = err.response.data
        this.usernameError = true
      }
    },
    async checkEmail() {
      try {
        await this.$axios.get(`users/check_availability/?email=${this.email}`)
        this.emailErrorMessages = ''
        this.emailError = false
      } catch (err) {
        this.emailErrorMessages = err.response.data
        this.emailError = true
      }
    },
  },
}
</script>

<style scoped lang="scss"></style>
