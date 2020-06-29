<template>
  <v-row justify="center" align="center">
    <v-col cols="12" md="6" lg="4">
      <v-card flat>
        <v-card-title class="title">
          <slot name="title" />
        </v-card-title>
        <v-card-text>
          <slot />
        </v-card-text>
        <v-card-actions>
          <slot name="help" />
          <v-spacer />
          <slot name="proceed" />
        </v-card-actions>
      </v-card>
      <p class="text-center mt-3">
        <slot name="alternateNavigation" />
      </p>
    </v-col>
  </v-row>
</template>

<script>
export default {}
</script>

<style scoped lang="scss"></style>
