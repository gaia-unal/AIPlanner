<template>
  <div style="margin-top:80px">
    <div class="accordion" id="accordionExample">
      <div class="card">
        <div class="bg-light" id="headingOne">
          <h2 class="mb-0">
            <button class="btn btn-link text-dark" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
              Problema
            </button>
          </h2>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne">
          <div class="container my-4">
            <app-problem :problem="problem"></app-problem>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="bg-light" id="headingTwo">
          <h2 class="mb-0">
            <button class="btn btn-link text-dark collapsed" type="button" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="true" aria-controls="collapseTwo">
              Dominio
            </button>
          </h2>
        </div>
        <div id="collapseTwo" class="collapse show" aria-labelledby="headingTwo">
          <div class="container my-4">
            <app-domain :problem="problem"></app-domain>
          </div>
          <button class="btn btn-success float-right m-3" @click="sendData">Run</button>
        </div>
      </div>
      <div class="card">
        <div class="bg-light" id="headingThree">
          <h2 class="mb-0">
            <button class="btn btn-link text-dark collapsed" type="button" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
              Salida
            </button>
          </h2>
        </div>
        <div id="collapseThree" class="collapse show" aria-labelledby="headingThree">
          <div class="container my-4">
            <ul v-for="(value, key) in problem.output" :key="value.id">
              <li :class="{invalid: key == 'Error'}">{{ key }}: {{ value }}</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Problem from './../components/strip/Problem.vue'
import Domain from './../components/strip/Domain.vue'

export default {
  mounted () {
    this.$store.dispatch('clearError')

    let problem = this.$store.getters.getCurrentProblem
    if (problem) {
      this.problem = problem
      this.$store.dispatch('setCurrentProblem', null)
    }
    /* this.problem.name = 'aspiradora'
    this.problem.initialState = [
      {
        name: "aspiradoraEn",
			  value: "L"
		  },
		  {
			  name: "sucio",
			  value: "L"
		  },
		  {
        name: "sucio",
        value: "R"
      }
    ]
    this.problem.finalState = [
		  {
			  name: "limpio",
			  value: "L"
		  },
		  {
        name: "limpio",
        value: "R"
      }
    ]
    this.problem.actions = [
      {
        name: "moverAspiradoraA",
        variables: "X,Y",
        preconditions: [
          {
            name: "aspiradoraEn",
            value: "X"
          }
        ],
        postconditions: [
          {
            name: "aspiradoraEn",
            value: "Y"
          },
          {
            name: "!aspiradoraEn",
            value: "X"
          }
        ]
      },
      {
        name: "limpiar",
        variables: "X",
        preconditions: [
          {
            name: "sucio",
            value: "X"
          },
          {
            name: "aspiradoraEn",
            value: "X"
          }
        ],
        postconditions: [
          {
            name: "limpio",
            value: "X"
          },
          {
            name: "!sucio",
            value: "X"
          }
        ]
      }
    ] */
  },
  data () {
    return {
      problem: {
        name: '',
        initialState: [],
        finalState: [],
        actions: [],
        output: {}
      }
    }
  },
  methods: {
    sendData () {
      if (this.problem.name.length > 0 && this.problem.initialState.length > 0 && this.problem.finalState.length > 0 && this.problem.actions.length > 0) {
        this.problem.output = {}
        this.$store.dispatch('clearError')
        this.$store.dispatch('sendStripProblem', this.problem)
      } else {
        this.problem.output = {}
        this.problem.output = {Error: 'Todos los campos anteriores son requeridos'}
      }
    }
  },
  components: {
    'app-problem': Problem,
    'app-domain': Domain
  }
}
</script>
<style>

  .invalid-input {
    border: 1px solid #dc3545;
  }

</style>
