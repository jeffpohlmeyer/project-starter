<template>
  <v-btn
    :color="color"
    :disabled="disabled"
    :loading="loading"
    :class="buttonClass"
    :to="to"
    :small="small"
    :rounded="rounded"
    :outlined="outlined"
    :text="text"
    :nuxt="nuxt"
    :block="block"
    @click="click"
  >
    <slot />
  </v-btn>
</template>

<script>
export default {
  props: {
    color: {
      type: String,
      required: false,
      default: '',
    },
    disabled: {
      type: Boolean,
      required: false,
      default: () => false,
    },
    loading: {
      type: Boolean,
      required: false,
      default: () => false,
    },
    classString: {
      type: String,
      required: false,
      default: '',
    },
    to: {
      type: String,
      required: false,
      default: '',
    },
    small: {
      type: Boolean,
      required: false,
      default: () => true,
    },
    rounded: {
      type: Boolean,
      required: false,
      default: () => true,
    },
    outlined: {
      type: Boolean,
      required: false,
      default: () => false,
    },
    text: {
      type: Boolean,
      required: false,
      default: () => false,
    },
    nuxt: {
      type: Boolean,
      required: false,
      default: () => false,
    },
    block: {
      type: Boolean,
      required: false,
      default: () => false,
    },
  },
  computed: {
    buttonClass() {
      return `text-capitalize ${this.classString}`
    },
  },
  methods: {
    click() {
      this.$emit('click')
    },
  },
}
</script>

<style scoped lang="scss"></style>
