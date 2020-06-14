<template>
  <div style="margin-top:80px">
    <div class="accordion" id="accordionExample">
      <div class="card">
        <div class="bg-light" id="headingOne">
          <h2 class="mb-0">
            <button class="btn btn-link text-dark" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
              Dominio
            </button>
          </h2>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne">
          <div class="container my-4">
            <app-methods :problem="problem"></app-methods>
            <app-operators :problem="problem" class="mt-4"></app-operators>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="bg-light" id="headingTwo">
          <h2 class="mb-0">
            <button class="btn btn-link text-dark collapsed" type="button" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="true" aria-controls="collapseTwo">
              Problema
            </button>
          </h2>
        </div>
        <div id="collapseTwo" class="collapse show" aria-labelledby="headingTwo">
          <div class="container my-4">
            <app-problem :problem="problem"></app-problem>
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
import Problem from './../components/htn/Problem.vue'
import Methods from './../components/htn/Methods.vue'
import Operators from './../components/htn/Operators.vue'

export default {
  mounted () {
    this.$store.dispatch('clearError')

    let problem = this.$store.getters.getCurrentProblem
    if (problem) {
      this.problem = problem
      this.$store.dispatch('setCurrentProblem', null)
    }

    /* this.problem = {
      "name": "viajar",
      "initialState": [
        {
          "name": "estar",
          "value": ["Manizales"]
        },
        {
          "name": "aeropuerto",
          "value": ["Manizales", "La nubia"]
        },
        {
          "name": "aeropuerto",
          "value": ["Bogota", "El dorado"]
        }
      ],
      "tasks": [
        {
          "name": "viajarEnAvion",
          "value": ["Manizales", "Bogota"]
        }
      ],
      "methods" : [
        {
          "name" : "viajarEnAvion",
          "variables" : ["x", "y"],
          "preconditions" : [
            {
              "name" : "aeropuerto",
              "value" : ["x", "a"]
            },
            {
              "name" : "aeropuerto",
              "value" : ["y", "b"]
            },
            {
              "name" : "estar",
              "value" : ["x"]
            }
          ],
          "postconditions" : [
            {
              "name" : "comprarTiquete",
              "value" : ["a", "b"]
            },
            {
              "name" : "viajar",
              "value" : ["x", "a"]
            },
            {
              "name" : "volar",
              "value" : ["a", "b"]
            },
            {
              "name" : "viajar",
              "value" : ["b", "y"]
            }
          ]
        },
        {
          "name" : "viajar",
          "variables" : ["x", "y"],
          "preconditions" : [
            {
              "name" : "estar",
              "value" : ["x"]
            }
          ],
          "postconditions" : [
            {
              "name" : "conseguirTaxi",
              "value" : ["x"]
            },
            {
              "name" : "irTaxi",
              "value" : ["x", "y"]
            }
          ]
        }
      ],
      "operators": [
        {
          "name": "comprarTiquete",
          "variables" : ["x", "y"],
          "preconditions" : [
            {
              "name": "aeropuerto",
              "value": ["a", "x"]
            },
            {
              "name": "aeropuerto",
              "value": ["b", "y"]
            }
          ],
          "del":[],
          "add":[
            {
              "name": "tenerTiquete",
              "value": ["x", "y"]
            }
          ]
        },
        {
          "name" : "volar",
          "variables" : ["x", "y"],
          "preconditions" : [
            {
              "name" : "estar",
              "value" : ["x"]
            },
            {
              "name" : "tenerTiquete",
              "value" : ["x", "y"]
            }
          ],
          "del" : [
            {
              "name" : "estar",
              "value" : ["x"]
            },
            {
              "name" : "tenerTiquete",
              "value" : ["x", "y"]
            }
          ],
          "add": [
            {
              "name" : "estar",
              "value" : ["y"]
            }
          ]
        },
        {
          "name" : "conseguirTaxi",
          "variables" : ["x"],
          "preconditions" : [
            {
              "name" : "estar",
              "value" : ["x"]
            }
          ],
          "del" : [],
          "add": [
            {
              "name" : "taxi",
              "value" : ["x"]
            }
          ]
        },
        {
          "name" : "irTaxi",
          "variables" : ["x", "y"],
          "preconditions" : [
            {
              "name" : "taxi",
              "value" : ["x"]
            },
            {
              "name" : "estar",
              "value" : ["x"]
            }
          ],
          "del" : [
            {
              "name" : "taxi",
              "value" : ["x"]
            },
            {
              "name" : "estar",
              "value" : ["x"]
            }
          ],
          "add": [
            {
              "name" : "estar",
              "value" : ["y"]
            }
          ]
        }
      ],
      "output": {}
    } */

  },
  data () {
    return {
      problem: {
        name: '',
        initialState: [],
        tasks: [],
        methods: [],
        operators: [],
        output: {}
      }
    }
  },
  methods: {
    sendData () {
      if (this.problem.name.length > 0 && this.problem.initialState.length > 0 && this.problem.tasks.length > 0 && this.problem.methods.length > 0 && this.problem.operators.length > 0) {
        this.problem.output = {}
        this.$store.dispatch('clearError')
        this.$store.dispatch('sendHtnProblem', this.problem)
      } else {
        this.problem.output = {}
        this.problem.output = {Error: 'Todos los campos anteriores son requeridos'}
      }
    }
  },
  components: {
    'app-problem': Problem,
    'app-methods': Methods,
    'app-operators': Operators
  }
}
</script>
<style >

.invalid-input {
    border: 1px solid #dc3545;
  }

</style>