<template>
    <li class="bold"><a class="collapsible-header waves-effect waves-purple lighten-3">Курсы</a>
        <div class="collapsible-body">
            <ul  v-for="category in listCategories.result" :key="category.id">
                <li><a href="">{{ category.name }}</a></li>
            </ul>
        </div>
    </li>
</template>

<script>
export default {
  data () {
    return {
      listCategories: []
    }
  },
  created() {
    this.getCategory()
  },
  methods: {
    async getCategory () {
       await fetch(`${this.$store.getters.getServerUrl}/category/`)
        .then(response => response.json())
        .then(resdata => this.listCategories.result = resdata)
        console.log("TARGET", this.listCategories)
    }
  }
}
</script>