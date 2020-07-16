<template>
  <div style="margin-top:80px">
    <div class="row">
      <div class="col-md-6">
        <h2>STRIPS</h2>
          <ul class="list-group" v-for="(problem, key) in problems.strip" :key="problem.id">
            <li class="list-group-item list-group-item-action">
              <div class="row">
                <div class="col-md-7 my-auto">
                  {{ key }}
                </div>
                <div class="col-md-5">
                  <button class="btn btn-outline-success mr-2" @click="seeProblemStrip(problem)">Ver</button>
                  <button class="btn btn-outline-danger" data-toggle="modal" data-target="#modal" @click="stripKey = key">Eliminar</button>
                </div>
              </div>
            </li>
          </ul>
      </div>
      <div class="col-md-6">
        <h2>HTN</h2>
          <ul class="list-group" v-for="(problem, key) in problems.htn" :key="problem.id">
            <li class="list-group-item list-group-item-action">
              <div class="row">
                <div class="col-md-7 my-auto">
                  {{ key }}
                </div>
                <div class="col-md-5">
                  <button class="btn btn-outline-success mr-2" @click="seeProblemHtn(problem)">Ver</button>
                  <button class="btn btn-outline-danger" data-toggle="modal" data-target="#modal" @click="htnKey = key">Eliminar</button>
                </div>
              </div>
            </li>
          </ul>
      </div>
    </div>
    <!-- Alert -->
    <div class="modal fade" id="modal" tabindex="-1" role="dialog" aria-labelledby="modalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            ¿Eliminar permanentemente?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
            <button type="button" class="btn btn-primary" data-dismiss="modal" @click="deleteProblem">Aceptar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  created () {
    this.$store.dispatch('getProblems')
  },
  data () {
    return {
      stripKey: null,
      htnKey: null
    }
  },
  computed: {
    problems () {
      return this.$store.getters.getProblems
    }
  },
  methods: {
    deleteProblem () {
      if (this.stripKey) {
        this.$store.dispatch('deleteProblem', {
          type: 'strip',
          key: this.stripKey
        })
        this.stripKey = null
      }
      if (this.htnKey) {
        this.$store.dispatch('deleteProblem', {
          type: 'htn',
          key: this.htnKey
        })
        this.htnKey = null
      }
    },
    seeProblemStrip (problem) {
      this.$store.dispatch('setCurrentProblem', problem)
      this.$router.push('strip')
    },
    seeProblemHtn (problem) {
      this.$store.dispatch('setCurrentProblem', problem)
      this.$router.push('htn')
    }
  }
}
</script>