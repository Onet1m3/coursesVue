<template>
    <li class="bold"><a class="collapsible-header waves-effect waves-purple lighten-3">Онлайн школы</a>
        <div class="collapsible-body">
            <ul v-for="school in listSchools.result" :key="school.id">
                <li><router-link :to="`/school/${school.slug}`">{{ school.title }}</router-link></li>
                
            </ul>
        </div>
    </li>
</template>

<script>
export default {
  data () {
    return {
      listSchools: []
    }
  },
  created() {
    this.getSchool()
  },
  methods: {
    async getSchool () {
       await fetch(`${this.$store.getters.getServerUrl}/school/`)
        .then(response => response.json())
        .then(resdata => this.listSchools.result = resdata)
        console.log(this.listSchools)
    }
  }
}
</script>