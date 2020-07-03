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
  props: {
    loading: {
      type: Boolean,
      required: true,
      default: false,
    },
  },
  data: () => ({
    email: '',
    valid: true,
  }),
  methods: {
    reset() {
      if (this.$refs.form.validate()) {
        this.$emit('triggerForgotEvent', this.email)
      }
    },
  },
}
</script>

<style scoped lang="scss"></style>
