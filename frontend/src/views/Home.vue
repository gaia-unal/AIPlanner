<template>
  <div class="text-center">
    <p class="h1 text-secondary" style="margin-top:200px">Ambiente gráfico de planificación basado en STRIPS y HTN</p>
    <button class="btn btn-success btn-lg mt-3" @click="goToLogin">Regístrate</button>
  </div>
</template>
<script>
export default {
  methods: {
    goToLogin () {
      if (!this.$store.getters.isAuthenticated) {
        this.$router.push('auth/sign-up')
      }
    }
  }
}
</script>