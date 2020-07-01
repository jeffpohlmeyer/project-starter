<template>
  <v-form ref="form" v-model="valid">
    <BaseUserComponent>
      <v-row justify="space-between" no-gutters>
        <v-col cols="12">
          <UsernameTextField
            v-model="username"
            autofocus
            @enterPressed="login"
          />
        </v-col>
        <v-col cols="12">
          <PasswordTextField v-model="password" @enterPressed="login" />
          <p class="text-center">
            <nuxt-link to="forgot-password">Forgot password?</nuxt-link>
          </p>
        </v-col>
      </v-row>
      <template v-slot:title>
        Log In
      </template>
      <template v-slot:proceed>
        <base-button
          class="text-capitalize"
          :loading="loading"
          block
          :small="false"
          @click="login"
        >
          Login
        </base-button>
      </template>
      <template v-slot:alternateNavigation>
        Don't have an account yet? Click
        <nuxt-link to="sign-up">here</nuxt-link> to sign up.
      </template>
    </BaseUserComponent>
  </v-form>
</template>

<script>
import { mapMutations } from 'vuex'
import PasswordTextField from '~/components/functional-components/PasswordTextField.vue'
import UsernameTextField from '~/components/functional-components/UsernameTextField'

export default {
  components: {
    UsernameTextField,
    PasswordTextField,
    BaseUserComponent: () => import('~/components/user/BaseUserComponent.vue'),
  },
  data: () => ({
    username: '',
    password: '',
    loading: false,
    valid: true,
  }),
  methods: {
    ...mapMutations({
      setSnackbarData: 'setSnackbarData',
      setAccess: 'auth/setAccess',
      setRefresh: 'auth/setRefresh',
    }),
    async login() {
      if (this.$refs.form.validate()) {
        this.loading = true
        try {
          const response = await this.$axios.$post('auth/jwt/create/', {
            username: this.username,
            password: this.password,
          })
          this.$axios.setHeader('Authorization', `Bearer ${response.access}`)
          this.setAccess(response.access)
          this.setRefresh(response.refresh)
          await this.$axios.$get('auth/users/me/')
          await this.$router.push('/user')
        } catch (err) {
          let message
          const snackbar = true
          try {
            message =
              err.response.data.error || 'Email or password is incorrect.'
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
