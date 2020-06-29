<template>
  <v-form ref="form" v-model="valid">
    <BaseUserComponent>
      <EmailTextField v-model="email" autofocus @enterPressed="reset" />
      <template v-slot:title>
        Confirm Email
      </template>
      <template v-slot:proceed>
        <base-button :loading="loading" block @click="reset">
          Send Email
        </base-button>
      </template>
    </BaseUserComponent>
  </v-form>
</template>

<script>
import EmailTextField from '~/components/functional-components/EmailTextField'

export default {
  components: {
    EmailTextField,
    BaseUserComponent: () => import('~/components/user/BaseUserComponent.vue'),
  },
  data: () => ({
    email: '',
    valid: true,
    loading: false,
  }),
  methods: {
    async reset() {
      this.loading = true
      try {
        await this.$axios.$post('user/forgot-password', {
          email: this.email,
        })
        await this.$router.push('notify')
      } catch (err) {
        // eslint-disable-next-line
        console.log('err', err)
      } finally {
        this.loading = false
      }
    },
  },
}
</script>

<style scoped lang="scss"></style>
