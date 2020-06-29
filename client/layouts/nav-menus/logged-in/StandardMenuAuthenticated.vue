<template>
  <div>
    <nuxt-link to="/user/log-out">Logout</nuxt-link>
  </div>
</template>

<script>
export default {
  methods: {
    async logout() {
      await this.$auth.logout()
    },
  },
}
</script>

<style scoped lang="scss"></style>
