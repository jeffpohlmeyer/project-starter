<template>
  <div>
    <base-button text :small="false" @click="logout">Logout</base-button>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$store.commit('auth/clearTokens')
    },
  },
}
</script>

<style scoped lang="scss"></style>
