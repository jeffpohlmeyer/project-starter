<template>
  <div>
    Placeholder
    <base-button @click="setToken">
      Set Token
    </base-button>
    LoggedIn {{ loggedIn }}
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters('auth', ['loggedIn']),
  },
  methods: {
    setToken() {
      this.$store.commit('auth/setAccess', 'test')
    },
  },
}
</script>
