<template>
  <div>
    <component :is="component" />
  </div>
</template>

<script>
  import { mapGetters } from 'vuex';

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
    ...mapGetters('auth',[
      'loggedIn'
    ]),
    mobile() {
      return this.$vuetify.breakpoint.xs
    },
    component() {
      if (this.loggedIn) {
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
