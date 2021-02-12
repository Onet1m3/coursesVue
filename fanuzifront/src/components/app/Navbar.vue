<template>
    <nav>
        <div class="container">
            <div class="nav-wrapper">
                <a href="#" data-target="slide-out" class="sidenav-trigger"><i class="material-icons">menu</i></a>
                <ul class="right">
                    <li><a href="">Форум</a></li>
                    <li><a href="">Новоcти</a></li>
                    <li v-if="!isAuthUser"><router-link to="/login"> <i class="large material-icons">person</i></router-link></li>
                    <li v-else-if="isAuthUser" @click="logout"><a><i class="large material-icons">exit_to_app</i></a></li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
import M from 'materialize-css/dist/js/materialize.min'

export default {
  data () {
    return {
      isAuthUser: false
    }
  },
  mounted () {
    const user = localStorage.getItem('token')
    if (user) {
      this.isAuthUser = true
    }
  },
  methods: {
    async logout() {
      await fetch(`${this.$store.getters.getServerUrl}/auth/logout/`, {
        headers: {
            'Content-Type': 'application/json',
            Authorization: "Token " + localStorage.getItem('token')
        },   
      })
        .then(response => response.json())
        .catch(err => {console.warn(err)})
        localStorage.removeItem('token')
        this.showToast()
        this.isAuthUser = false
    },
    showToast() {
      var toastHTML = "Вы вышли из системы"
      M.toast({html: toastHTML})
    }

  },
  beforeUnmount () {
    delete (this.isAuthUser)
  }
}
</script>
