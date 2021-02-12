<template>
    <div class="grey-custom empty-layout">
        <Form @submit="getLogin" :validation-schema="schema" v-slot="{ errors }" class="card auth-card">
            <div class="card-content">
                <span class="card-title center">Вход на сайт <router-link class="link-home" to="/">Fanuzi</router-link></span>
                <div class="input-field">
                    <Field
                        id="loginEmail"
                        name="email"
                        type="text"
                    />
                    <label for="loginEmail">Email</label>
                    <small class="helper-text invalid">
                      {{errors.email}}
                    </small>
                </div>
                <div class="input-field">
                    <Field
                        id="loginPassword"
                        type="password"
                        name="password"
                    />
                    <label for="loginPassword">Пароль</label>
                    <small class="helper-text invalid">{{errors.password}}</small>
                </div>
            </div>
            <div class="card-action">
                <div>
                    <button
                        class="btn waves-effect waves-light auth-submit"
                    >
                        Войти
                        <i class="material-icons right">send</i>
                    </button>
                </div>
                <p class="center">
                Нет аккаунта?
                <router-link to="/register">Зарегистрироваться</router-link>
                </p>
            </div>
        </form>
    </div>
    <!-- Modal -->
    <div id="loginModal" class="modal">
      <div class="modal-content">
        <h4 class="center">{{ modalHeaderText }}</h4>
        <p class="center">{{ modalBodyText }}</p>
      </div>
      <div class="modal-footer">
        <a @click.prevent="authLogin" class="waves-effect waves-green btn-flat">Ok</a>
      </div>
    </div>
</template>

<script>
import { Field, Form } from 'vee-validate'
import * as yup from 'yup'
import M from 'materialize-css/dist/js/materialize.min'

export default {
  data () {
    const schema = yup.object({
      email: yup.string().required().email(),
      password: yup.string().required().min(8)
    })
    return {
      modalHeaderText: "",
      modalBodyText: "",
      isSuccsess: "",
      schema
    }
  },
  methods: {
    async getLogin (values) {
      const formData = {
        username: values.email.toLowerCase(),
        password: values.password
      }
      await fetch(`${this.$store.getters.getServerUrl}/auth/token/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      })
        .then(response => response.json())
        .then(data => { 
          if(data.token) {
            localStorage.setItem('token', data.token)
            this.modalHeaderText = "Вы успешно залогинены!"
            this.modalBodyText =  "Вы будите перенаправлены на главную страницу"
            this.isSuccsess = true
            this.showModalWindow ()
            
          }
          else {
            this.modalHeaderText = "В этот раз у вас не получилось хакнуть аккаунт"
            this.modalBodyText =  "Не расстраивайтесь, с каждой попыткой остается все меньше комбинаций, попробуйте еще раз"
            this.isSuccsess = false
            this.showModalWindow ()
          }
        })
        .catch(err => { 
          this.modalHeaderText = "К сожалению наш сервер не хочет работать"
          this.modalBodyText = "Но мы уговариваем его изо всех сил, попробуйте позже"
          this.isSuccsess = false
          this.showModalWindow ()
        })
    },
    authLogin (token) {
      if (this.isSuccsess) {
        this.$router.push('/')
      } 
      else {
        this.closeModalWindow()
      }
    },
    showModalWindow () {
      var elems = document.getElementById('loginModal')
      var modal = M.Modal.init(elems, { preventScrolling:false, dismissible:false })
      modal.open()
    },
    closeModalWindow () {
      var elems = document.getElementById('loginModal')
      var modal = M.Modal.init(elems, {})
      modal.close()
    },
  },
  components: {
    Field,
    Form
  }
}
</script>
