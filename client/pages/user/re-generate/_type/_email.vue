<template>
  <BaseUserComponent>
    Click the button below to generate a new token.
    <template v-slot:title>
      Unidentified Token Error
    </template>
    <template v-slot:proceed>
      <base-button :loading="loading" block @click="reGenerate">
        Generate Token
      </base-button>
    </template>
  </BaseUserComponent>
</template>

<script>
export default {
  components: {
    BaseUserComponent: () => import('@/components/user/BaseUserComponent'),
  },
  data: () => ({
    loading: false,
  }),
  methods: {
    async reGenerate() {
      this.loading = true
      try {
        await this.$axios.$post('user/re-generate', {
          email: this.$route.params.email,
          regenerateType: this.$route.params.type,
        })
        await this.$router.push('/user/notify')
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
      } finally {
        this.loading = false
      }
    },
  },
}
</script>

<style scoped></style>
