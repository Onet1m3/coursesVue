<template>
    <li class="bold"><a class="collapsible-header waves-effect waves-purple lighten-3">Онлайн школы</a>
        <div class="collapsible-body">
            <ul v-for="school in listSchools.result" :key="school.id">
                <li><a :href="`/school/${school.slug}`">{{ school.title }}</a></li> 
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
        .catch(error => console.log(error))
    }
  }
}
</script>