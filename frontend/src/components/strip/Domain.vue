<template>
  <div>
    <h5 class="">Agregar acciones</h5>
    <div class="border p-4">
      <div class="form-group row">
        <label class="col-md-4 my-auto" for="nameAction">Nombre</label>
        <div class="col-md-4">
          <input
            type="text"
            id="nameAction"
            class="form-control"
            v-model="actionName"
            :class="{'invalid-input': actionInvalid}"
            placeholder="nombre de la acción"
            >
        </div>
      </div>
      <div class="form-group row">
        <label for="nameVar" class="col-md-4 my-auto">Variables que recibe</label>
        <div class="col-md-4">
          <input
            type="text"
            id="nameVar"
            class="form-control"
            v-model="actionVar"
            :class="{'invalid-input': actionInvalid}"
            placeholder="variable1, variable2, etc"
          >
        </div>
      </div>
      <div class="form-group row">
        <label for="precondition" class="col-md-4 my-auto">Qué se debe cumplir</label>
        <div class="col-md-2">
          <select
            id="precondition"
            class="form-control"
            v-model="preconditionAf"
            :class="{'invalid-input': actionInvalid}"
          >
            <option selected value="null">Seleccionar</option>
            <option v-for="affirmation in problem.initialState" :key="affirmation.id" :value="affirmation.name">{{ affirmation.name }}</option>
            <option v-for="affirmation in problem.finalState" :key="affirmation.id" :value="affirmation.name">{{ affirmation.name }}</option>
          </select>
        </div>
        <div class="col-md-2">
          <input
            class="form-control"
            v-model="preconditionVr"
            :class="{'invalid-input': actionInvalid}"
          >
        </div>
        <button class="btn btn-success col-md-1.5" @click="addPrecondition">Agregar</button>
      </div>
      <div class="form-group row">
        <div class="col-md-4"></div>
        <div class="col-md-6">
          <ul class="list-group" v-if="preconditions.length > 0">
          <li class="list-group-item" v-for="(item, index) in preconditions" :key="item.id">
            <div class="form-group row" style="margin-bottom: 0px">
              <div class="col-md-4 my-auto">
                {{ item.name }}
              </div>
              <div class="col-md-4 my-auto">
                {{ item.value }}
              </div>
              <button class="btn btn-outline-danger col-md-1.5" style="margin-left: 8px" @click="deletePreconditionItem(index)">Eliminar</button>
            </div>
          </li>
        </ul>
        </div>
      </div>
      <div class="form-group row">
        <label for="postcondition" class="col-md-4 my-auto">Qué se logra</label>
        <div class="col-md-2">
          <select id="postcondition" class="form-control" :class="{'invalid-input': actionInvalid}" v-model="postconditionAf">
            <option selected value="null">Seleccionar</option>
            <option v-for="affirmation in problem.finalState" :key="affirmation.id" :value="affirmation.name">{{ affirmation.name }}</option>
            <option v-for="affirmation in problem.initialState" :key="affirmation.id" :value="affirmation.name">{{ affirmation.name }}</option>
            <option v-for="affirmation in problem.finalState" :key="affirmation.id" :value="'!'+affirmation.name">no-{{ affirmation.name }}</option>
            <option v-for="affirmation in problem.initialState" :key="affirmation.id" :value="'!'+affirmation.name">no-{{ affirmation.name }}</option>
          </select>
        </div>
        <div class="col-md-2">
          <input
            class="form-control"
            :class="{'invalid-input': actionInvalid}"
            v-model="postconditionVr"
          >
        </div>
        <button class="btn btn-success col-md-1.5" @click="addPostcondition">Agregar</button>
      </div>
      <div class="form-group row">
        <div class="col-md-4"></div>
        <div class="col-md-6">
          <ul class="list-group" v-if="postconditions.length > 0">
          <li class="list-group-item" v-for="(item, index) in postconditions" :key="item.id">
            <div class="form-group row" style="margin-bottom: 0px">
              <div class="col-md-4 my-auto">
                {{ item.name }}
              </div>
              <div class="col-md-4 my-auto">
                {{ item.value }}
              </div>
              <button class="btn btn-outline-danger col-md-1.5" style="margin-left: 8px" @click="deletePostconditionItem(index)">Eliminar</button>
            </div>
          </li>
        </ul>
        </div>
      </div>
      <div class="form-group row">
        <div class="col-md-12">
          <button class="btn btn-success float-right" @click="addAction">Agregar acción</button>
        </div>
      </div>
    </div>
    <div class="border p-4 mt-1" v-if="problem.actions.length > 0">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Nombre</th>
            <th scope="col">Variables</th>
            <th scope="col">Precondición</th>
            <th scope="col">Postcondición</th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(action, index) in problem.actions" :key="action.id">
            <td class="align-middle">{{ action.name }}</td>
            <td class="align-middle">{{ action.variables }}</td>
            <td class="align-middle">
              <p class="mb-0" v-for="item in action.preconditions" :key="item.id">{{ item.name }}({{ item.value }})</p></td>
            <td class="align-middle">
              <p class="mb-0" v-for="item in action.postconditions" :key="item.id">{{ item.name }}({{ item.value }})</p>
            </td>
            <td><button class="btn btn-outline-danger" @click="deleteAction(index)">Eliminar</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
export default {
  props: ['problem'],
  data () {
    return {
      preconditions: [],
      preconditionAf: null,
      preconditionVr: null,
      postconditions: [],
      postconditionAf: null,
      postconditionVr: null,
      actionName: '',
      actionVar: '',
      actionInvalid: false
    }
  },
  methods: {
    addPrecondition () {
      if (this.preconditionAf.length > 0 && this.preconditionVr.length > 0) {
        this.preconditions.push({
          name: this.preconditionAf,
          value: this.preconditionVr
        })
      }
    },
    deletePreconditionItem (index) {
      this.preconditions.splice(index, 1)
    },
    addPostcondition () {
      if (this.postconditionAf.length > 0 && this.postconditionVr.length > 0) {
        this.postconditions.push({
          name: this.postconditionAf,
          value: this.postconditionVr
        })
      }
    },
    deletePostconditionItem (index) {
      this.postconditions.splice(index, 1)
    },
    addAction () {
      if (this.actionName.length > 0 && this.actionVar.length > 0 && this.postconditions.length > 0) {
        this.problem.actions.push({
          name: this.actionName,
          variables: this.actionVar,
          preconditions: this.preconditions.slice(),
          postconditions: this.postconditions.slice()
        })
        this.actionName = ''
        this.actionVar = ''
        this.preconditionAf = null
        this.preconditionVr = null
        this.postconditionAf = null
        this.postconditionVr = null
        this.preconditions = []
        this.postconditions = []
        this.actionInvalid = false
      } else {
        this.actionInvalid = true
      }
    },
    deleteAction (index) {
      this.problem.actions.splice(index, 1)
    }
  }
}

</script>
