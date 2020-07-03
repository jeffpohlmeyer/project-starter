<template>
  <v-text-field
    :value="value"
    :label="label"
    dense
    rounded
    outlined
    :rules="rules"
    counter
    :hint="hint"
    validate-on-blur
    :autofocus="autofocus"
    append-outer-icon="mdi-account-outline"
    :error="error"
    :error-messages="errorMessages"
    @input="input"
    @keydown.enter.prevent="keydown('enterPressed')"
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
    hint: {
      type: String,
      required: false,
      default: 'Required',
    },
    label: {
      type: String,
      required: false,
      default: 'Username',
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
    usernameCompare: {
      type: String,
      required: false,
      default: '',
    },
  },
  computed: {
    rules() {
      const baseRules = [(v) => !!v || 'Required']
      return this.usernameCompare
        ? [
            ...baseRules,
            (v) => v === this.usernameCompare || 'Usernames must match',
          ]
        : baseRules
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
