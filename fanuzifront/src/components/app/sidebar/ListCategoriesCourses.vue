<template>
    <Loader v-if="loading" />
    <div>{{this.slug}}</div>
    <p>HLKHLGLGLLLJ</p>
    
</template>

<script>
import Loader from '@/components/Loader'
export default {
    props: ['slug'],
    data () {
        return {
            courses: [],
            url: this.$store.getters.getServerUrl,
            loading: false
        }
    },
    created () {
        this.getListCategoriesCourses()
    },
    methods: {
        async getListCategoriesCourses() {
            this.loading = true
            try {
                await fetch(`${this.url}/course/${this.slug}/`)
                    .then(response => response.json())
                    .then(resdata => this.courses = resdata)
                    console.log(this.courses)
                    this.loading = false
            }catch (e) {
                this.loading = false
                console.log(e.message)
            }
        }
    },
    components: {
        Loader
    }
}
</script>