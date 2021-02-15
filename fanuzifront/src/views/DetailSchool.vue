<template>
    <div class="card__presentations">
        <div class="col s12 m12 l12 xl12">
            <div class="card-panel">
                <div class="card__title">
                    <h2 class="card__title-title">{{ school.title }}</h2>
                </div>
                <div class="card__title-content">
                    <span class="card__title-text">I am a very simple card. I am good at containing small bits of information.
                        I am convenient because I require little markup to use effectively. I am similar to what is called a panel in other frameworks.
                    </span>
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
import {watch} from "vue"
export default {
    props: ['slug'],
    setup(props) {
        watch(() => props.slug, (first, second) => {
            console.log(props.slug)
            location.reload()
        })
    },
    data () {
        return {
            school: [],
            url: this.$store.getters.getServerUrl, 
        }
    },
    created() {
        this.getPost()
    },
    methods: {
        async getPost() {
            await fetch(`${this.url}/school/${this.slug}/`)
            .then(response => response.json())
            .then(resdata => this.school = resdata)
        }
    }
    
}
</script>