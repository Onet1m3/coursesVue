<template>
    <div class="grey-custom empty-layout register-card">
        <Form @submit="regUser" :validation-schema="schema" v-slot="{ errors }" class="card auth-card">
          <div v-show="preLoader" class="preloader-wrapper big active">
            <div class="spinner-layer spinner-deep-purple-only">
              <div class="circle-clipper left">
                <div class="circle"></div>
              </div>
              <div class="gap-patch">
                <div class="circle"></div>
              </div>
              <div class="circle-clipper right">
                <div class="circle"></div>
              </div>
            </div>
          </div>
            <div class="card-content">
                <span class="card-title center">Регистрация на сайте <router-link class="link-home" to="/">Fanuzi</router-link></span>
                <div class="input-field">
                    <Field
                        id="registerName"
                        type="text"
                        class="validate"
                        name="Name"
                    />
                    <label for="registerName">Имя</label>
                    <small class="helper-text invalid">{{errors.Name}}</small>
                </div>
                <div class="input-field">
                    <Field
                        id="registerEmail"
                        name="Email"
                        type="text"
                        class="validate"
                    />
                    <label for="registerEmail">Email</label>
                    <small class="helper-text invalid">{{errors.Email}}</small>
                </div>
                <div class="input-field">
                    <Field
                        id="registerPassword"
                        type="password"
                        name="password"
                        class="validate"
                    />
                    <label for="registerPassword">Пароль</label>
                    <small class="helper-text invalid">{{errors.password}}</small>
                </div>
                <div class="input-field">
                    <Field
                        id="registerConfirmPassword"
                        type="password"
                        name="confirmPassword"
                        class="validate"
                    />
                    <label for="registerConfirmPassword">Повторите пароль</label>
                    <small class="helper-text invalid">{{errors.confirmPassword}}</small>
                </div>
                <p>
                    <label>
                        <Field name="acceptTerms" type="checkbox" value="true" />
                        <span>С правилами согласен</span>
                    </label>
                </p>
                <small class="helper-text invalid">{{errors.acceptTerms}}</small>
            </div>
            <div class="card-action">
                <div>
                    <button
                        class="btn waves-effect waves-light auth-submit"
                    >
                        Зарегистрироваться
                        <i class="material-icons right">send</i>
                    </button>
                </div>

                <p class="center">
                Уже есть аккаунт?
                <router-link to="/login">Войти!</router-link>
                </p>
            </div>
        </Form>
    </div>
    <!-- Modal -->
    <div id="loaderModal" class="modal">
      <div class="modal-content">
        <h4 class="center">{{ modalHeaderText }}</h4>
        <p class="center">{{ modalBodyText }}</p>
      </div>
      <div class="modal-footer">
        <a @click.prevent="redirectToLogin" class="waves-effect waves-green btn-flat">Ok</a>
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
      Name: yup.string().required(),
      Email: yup.string().required().email(),
      password: yup.string().required().min(8),
      confirmPassword: yup.string().oneOf([yup.ref('password'), null], 'Passwords must match').required(),
      acceptTerms: yup.string().required()
    })
    return {
      modalHeaderText: "",
      modalBodyText: "",
      redirectUrl: "",
      isSuccsess: "",
      preLoader: false,
      schema
    }
  },
  methods: {
    async regUser (values) {
      const formData = {
        first_name: values.Name,
        email: values.Email.toLowerCase(),
        password: values.password,
        acceptTerms: values.acceptTerms
      }
      await fetch(`${this.$store.getters.getServerUrl}/auth/register/`, {
        method: 'POST',
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      })
        .then(response => {
          response.json()
          this.preLoader = true

          if(response.status === 201) {
            this.preLoader = false
            this.modalHeaderText = "Вы успешно зарегистрировались!"
            this.modalBodyText = "Вы будите перенаправлены на страницу входа"
            this.redirectUrl = '/login'
            this.isSuccsess = true
            this.showModalWindow()
          }
          else if (response.status === 400) {
            this.preLoader = false
            this.modalHeaderText = "Регистрация не завершилась успехом"
            this.modalBodyText = "Почтовый адрес который вы указали при регистрации к сожалению занят"
            this.isSuccsess = false
            this.showModalWindow()
          }
           else if (response.status === 500) {
            this.preLoader = false
            this.modalHeaderText = "К сожалению наш сервер не хочет работать"
            this.modalBodyText = "Но мы уговариваем его изо всех сил, попробуйте позже"
            this.isSuccsess = false
            this.showModalWindow()
          }
        })
        .catch(err => {
          this.modalHeaderText = "К сожалению наш сервер не хочет работать"
          this.modalBodyText = "Но мы уговариваем его изо всех сил, попробуйте позже"
          this.isSuccsess = false
          this.showModalWindow()
        })
    },
    showModalWindow () {
      var elems = document.getElementById('loaderModal')
      var modal = M.Modal.init(elems, { preventScrolling:false, dismissible:false })
      modal.open()
    },
    closeModalWindow () {
      var elems = document.getElementById('loaderModal')
      var modal = M.Modal.init(elems, {})
      modal.close()
    },
    redirectToLogin () {
      if(this.isSuccsess) {
        this.$router.push(this.redirectUrl)
      } else {
        this.closeModalWindow ()
      }
    }
  },
  components: {
    Field,
    Form
  }
}
</script>
