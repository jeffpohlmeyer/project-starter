<template>
  <v-text-field
    :value="value"
    :label="label"
    dense
    rounded
    outlined
    :type="show ? 'text' : 'password'"
    :append-outer-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
    :rules="rules"
    counter
    :hint="hint"
    validate-on-blur
    :autofocus="autofocus"
    @input="input"
    @keydown.enter="keydown('enterPressed')"
    @click:append-outer="togglePasswordVisibility"
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
      default:
        'Between 8 and 128 characters.  Must include at least one of ! @ # ?',
    },
    label: {
      type: String,
      required: false,
      default: 'Password',
    },
    passwordCompare: {
      type: String,
      required: false,
      default: '',
    },
    autofocus: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  data: () => ({
    show: false,
  }),
  computed: {
    rules() {
      const baseRules = [
        (v) => !!v || 'Required',
        (v) => v.length >= 8 || 'Minimum 8 characters',
        (v) => v.length <= 128 || 'Maximum 128 characters',
      ]
      return this.passwordCompare
        ? [
            ...baseRules,
            (v) => v === this.passwordCompare || 'Passwords must match',
          ]
        : baseRules
    },
  },
  methods: {
    input(e) {
      this.$emit('input', e)
    },
    togglePasswordVisibility() {
      this.show = !this.show
    },
    keydown(value) {
      this.$emit(value)
    },
  },
}
</script>

<style scoped lang="scss"></style>
