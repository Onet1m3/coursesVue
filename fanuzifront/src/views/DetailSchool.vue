<template>
    <div class="card__presentations">
        <Loader v-if="loading" />
        <div class="col s12 m12 l12 xl12" v-else>
            <div class="card-panel">
                <div class="card__title">
                    <h2 class="card__title-title">{{ school.title }}</h2>
                </div>
                <div class="card__title-content">
                    <span class="card__title-text">{{ school.discription }}</span>
                    <p class="card__title-text"></p>
                </div>
                <div class="card__link">
                    <a class="card__link-href btn" :href="school.url" target="_blank">Перейти на сайт школы <i class="material-icons right">send</i></a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Loader from '@/components/Loader'
export default {
    props: ['slug'],
    data () {
        return {
            school: [],
            url: this.$store.getters.getServerUrl,
            loading: false
        }
    },
    created() {
        this.getPost()
    },
    methods: {
        async getPost() {
            this.loading = true
            try {
                await fetch(`${this.url}/school/${this.slug}/`)
                .then(response => response.json())
                .then(resdata => this.school = resdata)
                this.loading = false
            }catch (e) {
                console.log(e.message)
            }
            
        }
    },
    components: {
        Loader
    }
    
}
</script>
