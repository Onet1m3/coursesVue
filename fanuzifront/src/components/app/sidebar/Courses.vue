<template>
    <li v-for="category in listCategories.result" :key="category.id" class="bold"><a class="collapsible-header waves-effect waves-purple lighten-3">{{ category.name }}</a>
        <div class="collapsible-body">
            <ul  v-for="item in category.children" :key="item.id">
                <li><a class="truncate" :href="`/course/${item.slug}`">{{ item.name }}</a></li>
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
        .catch(error => console.log(error))
    }
  }
}
</script>