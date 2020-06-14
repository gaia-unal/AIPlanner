<template>
  <div class="fixed-top">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container">
        <router-link to="/" class="navbar-brand">AG Planning</router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse"   data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"  aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <router-link v-if="auth" to="/dashboard" tag="li" class="nav-item"><a class="nav-link">Tablero</a></router-link>
            <router-link to="/strip" tag="li" class="nav-item"><a class="nav-link">STRIP</a></router-link>
            <router-link to="/htn" tag="li" class="nav-item"><a class="nav-link">HTN</a></router-link>
            <router-link to="/about" tag="li" class="nav-item"><a class="nav-link">Acerca de</a></router-link>
          </ul>
          <ul v-if="!auth" class="navbar-nav ml-auto">
            <router-link to="/auth/login" tag="li" class="nav-item"><a class="nav-link">Inicia sesión</a></router-link>
            <router-link to="/auth/sign-up" tag="li" class="nav-item"><a class="nav-link">Regístrate</a></router-link>
          </ul>
          <ul v-if="auth" class="navbar-nav ml-auto">
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="false" aria-expanded="false" @click="showDropDown = !showDropDown">
                {{ name }}
              </a>
              <ul v-if="showDropDown" class="dropdown-menu" :class="{show: showDropDown}" style="width: 194px">
                <div v-if="!showChangePassword">
                  <li class="dropdown-item" @click="showChangePassword = true" style="cursor: pointer">Cambiar contraseña</li>
                  <div class="dropdown-divider"></div>
                  <li class="dropdown-item" @click="logout" style="cursor: pointer">Cerrar sesión</li>
                </div>
                <div v-if="showChangePassword">
                  <app-error v-if="error" :error="error"></app-error>
                  <div class="form-group">
                    <input
                      type="password"
                      class="form-control input"
                      placeholder="Contraseña actual"
                      @blur="$v.currentPassword.$touch()"
                      v-model="currentPassword"
                    >
                    <input
                      type="password"
                      class="form-control input"
                      placeholder="Contraseña nueva"
                      @blur="$v.newPassword.$touch()"
                      v-model="newPassword"
                    >
                  </div>
                  <div class="dropdown-divider"></div>
                  <li class="dropdown-item" style="cursor: pointer" @click="changePassword">Cambiar contraseña</li>
                  <div class="dropdown-divider"></div>
                  <li class="dropdown-item" @click="clearError" style="cursor: pointer">Cancelar</li>
                </div>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>
<script>
import { required, minLength } from 'vuelidate/lib/validators'
import MessageError from './../components/Error.vue'

export default {
  data () {
    return {
      currentPassword: '',
      newPassword: '',
      showChangePassword: false,
      showDropDown: null
    }
  },
  validations: {
    currentPassword: {
      required,
      minLength: minLength(6)
    },
    newPassword: {
      required,
      minLength: minLength(6)
    }
  },
  computed: {
    auth () {
      return this.$store.getters.isAuthenticated
    },
    name () {
      return this.$store.getters.name
    },
    error () {
      return this.$store.getters.headError
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('logout', this.$route.path)
      this.showDropDown = null
    },
    changePassword () {
      if (this.$v.$invalid) {
        this.$store.dispatch('updateHeadError', {
          message: 'La contraseña debe tener al menos 6 caracteres.'
        })
      } else {
        const formData = {
          currentPassword: this.currentPassword,
          newPassword: this.newPassword
        }
        this.$store.dispatch('changeData', formData)
        setTimeout(() => {
          if (!this.error) {
            this.showDropDown = null
            this.clearError()
          }
        }, 500)
      }
    },
    clearError () {
      this.$store.dispatch('clearError')
      this.showChangePassword = false
      this.currentPassword = ''
      this.newPassword = ''
    }
  },
  components: {
    'app-error': MessageError
  }
}
</script>
<style>
.input {
  width: 98% !important;
  margin: 1%;
}
</style>
