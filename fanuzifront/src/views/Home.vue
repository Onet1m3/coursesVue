<template>
    <Loader v-if="loading" />
    <div class="home" v-for="course in listCourses" :key="course.id" v-else>
        <div class="content__item_card col s12 m12 l12">
          <div class="card">
              <div class="card-image">
                  <img :src="course.school_name.picture" alt="">
              </div>
                  <div class="card-content">
                      <span class="card-title">{{course.title}}</span>
                      <p>Дата начала курса: {{course.date_start}} </p>
                      <p>Дата окончания курса: {{course.date_end}}</p>
                      <p>Стоимость: {{course.amount}}</p>
                  </div>
              <div class="card-action">
                  <a :href="course.school_name.url">Ссылка на курс</a>
              </div>
          </div>
      </div>
    </div>
</template>

<script>
import Loader from '../components/Loader'
export default {
    data () {
        return {
            listCourses: [],
            loading: false,
        }
    },
    mounted () {
        this.getCourseList()
    },
    methods: {
        async getCourseList () {
            this.loading = true
            await fetch(`${this.$store.getters.getServerUrl}/course/`)
            .then(response => response.json())
            .then(resdata => this.listCourses = resdata)
            .catch(error => console.log(error))
            this.loading = false
        }
    },
    components: {
        Loader
    }
}
</script>
