<template>
  <div>{{ abc }}</div>
</template>

<script>
export default {
  asyncData(context) {
    // eslint-disable-next-line
    const res = context.app.$axios.$get('users/auth/me/')
    return { abc: res.data }
  },
}
</script>

<style scoped lang="scss"></style>
