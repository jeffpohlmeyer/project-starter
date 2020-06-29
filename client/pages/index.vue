<template>
  <div>
    Placeholder
    <base-button @click="setToken">
      Set Token
    </base-button>
    IsLoggedIn {{ isLoggedIn }}
  </div>
</template>

<script>
export default {
  computed: {
    isLoggedIn() {
      return this.$auth.loggedIn
    },
  },
  methods: {
    setToken() {
      this.$auth.setToken('customStrategy', 'test')
    },
  },
}
</script>
