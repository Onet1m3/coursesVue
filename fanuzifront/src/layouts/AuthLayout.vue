<template>
    <div>
    <particles-bg type="cobweb" :bg="true" />
        <router-view />
    </div>
</template>

<script>
import { ParticlesBg } from 'particles-bg-vue'
export default {
  components: {
    ParticlesBg
  }
}
</script>