<template>
    <div class="main">
        <div class="navigate">
            <div class="navigate__bar">
                <div class="navigate__row-side">
                    <ul id="slide-out" class="sidenav sidenav-fixed" ref="sidenav">
                        <li>
                            <div class="user-view  indigo-theme">
                                <div class="navigate__title">
                                    <a href="/"><span class="navigate__title-name">Fanuzi</span></a>
                                </div>
                                <div class="navigate__suubtitle">
                                    <h1>Лучший сайт поиска онлайн курсов</h1>
                                </div>
                            </div>
                        </li>
                        <Sidebar />
                    </ul>
                </div>
                <div class="navigate__row-nav">
                   <Navbar />
                </div>
            </div>
        </div>
        <div class="content">
            <div class="content__row">
                <div class="content__item">
                    <router-view />
                </div>
            </div>
        </div>
        <Footer />
    </div>
</template>

<script>
import Navbar from '@/components/app/Navbar'
import Sidebar from '@/components/app/Sidebar'
import Footer from '@/components/app/Footer'
import M from 'materialize-css/dist/js/materialize.min'

export default {
  mounted () {
    M.Sidenav.init(this.$refs.sidenav, {})
  },
  components: {
    Navbar, Sidebar, Footer
  }
}

</script>
