<template>
  <div>Logging Out...</div>
</template>

<script>
export default {
  created() {
    this.$auth.logout()
  },
}
</script>

<style scoped lang="scss"></style>
