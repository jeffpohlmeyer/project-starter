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
      <template v-slot:title>Reset password</template>
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
import useErrorParser from '~/utils/parse-errors'
import PasswordTextField from '~/components/functional-components/PasswordTextField'

export default {
  components: {
    PasswordTextField,
    BaseUserComponent: () => import('~/components/user/BaseUserComponent.vue'),
  },
  data: () => ({
    valid: true,
    password: '',
    password2: '',
    loading: false,
    error: false,
  }),
  methods: {
    ...mapMutations({
      setSnackbarData: 'setSnackbarData',
    }),
    async updatePassword() {
      if (this.$refs.form.validate()) {
        let message = ''
        const snackbar = true
        let color
        this.loading = true
        try {
          await this.$axios.$post('users/auth/reset_password_confirm/', {
            uid: this.$route.params.uid,
            token: this.$route.params.token,
            new_password: this.password,
            re_new_password: this.password2,
          })
          await this.$router.push('/user/log-in')
          message =
            'You have successfully updated your password.  Please log in.'
          color = 'success'
        } catch (err) {
          try {
            message = useErrorParser(err.response)
          } catch {
            message =
              'There was an unidentified error.  Please try again later.'
          }
        } finally {
          this.setSnackbarData({
            snackbar,
            message,
            color,
          })
          this.loading = false
        }
      }
    },
  },
}
</script>

<style scoped lang="scss"></style>
