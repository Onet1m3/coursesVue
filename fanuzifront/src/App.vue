<template>
    <component :is="layout">
      <router-view/>
    </component>
</template>

<script>
import MainLayout from '@/layouts/MainLayout'
import AuthLayout from '@/layouts/AuthLayout'
export default {
  computed: {
    layout () {
      return (this.$route.meta.layout) + '-layout'
    }
  },
  components: {
    MainLayout, AuthLayout
  }
}
</script>

<style>
  @import '~materialize-css/dist/css/materialize.min.css';
  @import 'assets/css/main.css';
</style>
