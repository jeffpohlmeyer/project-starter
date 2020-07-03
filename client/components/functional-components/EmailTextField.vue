<template>
  <v-text-field
    :value="value"
    label="Email"
    :rules="emailRules"
    dense
    rounded
    outlined
    validate-on-blur
    :autofocus="autofocus"
    append-outer-icon="mdi-email"
    :error="error"
    :error-messages="errorMessages"
    @keydown.enter.prevent="keydown('enterPressed')"
    @input="input($event)"
    @blur="blur"
  />
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      required: true,
    },
    autofocus: {
      type: Boolean,
      required: false,
      default: false,
    },
    error: {
      type: Boolean,
      required: false,
      default: false,
    },
    errorMessages: {
      type: String || Array,
      required: false,
      default: '',
    },
  },
  computed: {
    emailRules() {
      return [
        (v) => !!v || 'Required',
        (v) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(v) || 'Invalid e-mail.'
        },
      ]
    },
  },
  methods: {
    input(e) {
      this.$emit('input', e)
    },
    keydown(value) {
      this.$emit(value)
    },
    blur() {
      this.$emit('blur')
    },
  },
}
</script>

<style scoped></style>
