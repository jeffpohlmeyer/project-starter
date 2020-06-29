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
    @input="input"
    @keydown.enter="keydown('enterPressed')"
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
  },
  computed: {
    rules() {
      return [(v) => !!v || 'Required']
    },
  },
  methods: {
    input(e) {
      this.$emit('input', e)
    },
    keydown(value) {
      this.$emit(value)
    },
  },
}
</script>

<style scoped></style>
