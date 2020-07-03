<template>
  <v-form ref="form" v-model="valid">
    <BaseUserComponent>
      <v-row justify="space-between" no-gutters>
        <v-col cols="12">
          <UsernameTextField
            v-model="username"
            autofocus
            @enterPressed="updateUsername"
          />
        </v-col>
        <v-col cols="12">
          <UsernameTextField
            v-model="username2"
            :password-compare="username"
            label="Confirm Username"
            @enterPressed="updateUsername"
          />
        </v-col>
      </v-row>
      <template v-slot:title>Reset username</template>
      <template v-slot:proceed>
        <base-button :loading="loading" block @click="updateUsername">
          Update Username
        </base-button>
      </template>
    </BaseUserComponent>
  </v-form>
</template>

<script>
import { mapMutations } from 'vuex'
import useErrorParser from '~/utils/parse-errors'
import UsernameTextField from '~/components/functional-components/UsernameTextField'

export default {
  components: {
    UsernameTextField,
    BaseUserComponent: () => import('~/components/user/BaseUserComponent.vue'),
  },
  data: () => ({
    valid: true,
    username: '',
    username2: '',
    loading: false,
    error: false,
  }),
  methods: {
    ...mapMutations({
      setSnackbarData: 'setSnackbarData',
    }),
    async updateUsername() {
      if (this.$refs.form.validate()) {
        let message = ''
        const snackbar = true
        let color
        this.loading = true
        try {
          await this.$axios.$post('users/auth/reset_username_confirm/', {
            uid: this.$route.params.uid,
            token: this.$route.params.token,
            new_username: this.username,
            re_new_username: this.username2,
          })
          await this.$router.push('/user/log-in')
          message =
            'You have successfully updated your username.  Please log in.'
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
