<template>
  <div>
    <component :is="component" />
  </div>
</template>

<script>
import MobileMenuAuthenticated from '~/layouts/nav-menus/logged-in/MobileMenuAuthenticated'
import StandardMenuAuthenticated from '~/layouts/nav-menus/logged-in/StandardMenuAuthenticated'
import MobileMenuUnauthenticated from '~/layouts/nav-menus/not-logged-in/MobileMenuUnauthenticated'
import StandardMenuUnauthenticated from '~/layouts/nav-menus/not-logged-in/StandardMenuUnauthenticated'

export default {
  components: {
    MobileMenuAuthenticated,
    MobileMenuUnauthenticated,
    StandardMenuAuthenticated,
    StandardMenuUnauthenticated,
  },
  computed: {
    isLoggedIn() {
      return this.$auth.loggedIn
    },
    mobile() {
      return this.$vuetify.breakpoint.xs
    },
    component() {
      if (this.isLoggedIn) {
        return this.mobile ? MobileMenuAuthenticated : StandardMenuAuthenticated
      }
      return this.mobile
        ? MobileMenuUnauthenticated
        : StandardMenuUnauthenticated
    },
  },
}
</script>

<style scoped lang="scss"></style>
