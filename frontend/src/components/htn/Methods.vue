<template>
  <div>
    <h5 class="">Agregar métodos</h5>
    <div class="border p-4">
      <div class="form-group row">
        <label class="col-md-4 my-auto" for="nameMethod">Nombre</label>
        <div class="col-md-4">
          <input
            type="text"
            id="nameMethod"
            class="form-control"
            v-model="methodName"
            :class="{'invalid-input': methodInvalid}"
            placeholder="nombre del método"
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
            v-model="methodVar"
            :class="{'invalid-input': methodInvalid}"
            placeholder="variable1, variable2, etc"
          >
        </div>
      </div>
      <div class="form-group row">
        <label for="precondition" class="col-md-4 my-auto">Qué se debe cumplir</label>
        <div class="col-md-2">
          <input
            type="text"
            id="precondition"
            class="form-control"
            v-model="preconditionAf"
            :class="{'invalid-input': methodInvalid}"
            placeholder="nombre"
          >
        </div>
        <div class="col-md-2">
          <input
            type="text"
            class="form-control"
            v-model="preconditionVr"
            :class="{'invalid-input': methodInvalid}"
            placeholder="variables"
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
        <label for="postcondition" class="col-md-4 my-auto">Qué se puede hacer</label>
        <div class="col-md-2">
          <input
            type="text"
            id="postcondition"
            class="form-control"
            :class="{'invalid-input': methodInvalid}"
            v-model="postconditionAf"
            placeholder="nombre"
          >
        </div>
        <div class="col-md-2">
          <input
            type="text"
            class="form-control"
            :class="{'invalid-input': methodInvalid}"
            v-model="postconditionVr"
            placeholder="variables"
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
          <button class="btn btn-success float-right" @click="addMethod">Agregar método</button>
        </div>
      </div>
    </div>
    <div class="border p-4 mt-1" v-if="problem.methods.length > 0">
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
          <tr v-for="(method, index) in problem.methods" :key="method.id">
            <td class="align-middle">{{ method.name }}</td>
            <td class="align-middle">{{ method.variables }}</td>
            <td class="align-middle">
              <p class="mb-0" v-for="item in method.preconditions" :key="item.id">{{ item.name }}{{ item.value }}</p></td>
            <td class="align-middle">
              <p class="mb-0" v-for="item in method.postconditions" :key="item.id">{{ item.name }}{{ item.value }}</p>
            </td>
            <td><button class="btn btn-outline-danger" @click="deleteMethod(index)">Eliminar</button></td>
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
      methodName: '',
      methodVar: '',
      methodInvalid: false
    }
  },
  methods: {
    addPrecondition () {
      if (this.preconditionAf.length > 0 && this.preconditionVr.length > 0) {
        this.preconditions.push({
          name: this.preconditionAf,
          value: this.preconditionVr.split(',')
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
          value: this.postconditionVr.split(',')
        })
      }
    },
    deletePostconditionItem (index) {
      this.postconditions.splice(index, 1)
    },
    addMethod () {
      if (this.methodName.length > 0 && this.methodVar.length > 0 && this.postconditions.length > 0) {
        this.problem.methods.push({
          name: this.methodName,
          variables: this.methodVar.split(','),
          preconditions: this.preconditions.slice(),
          postconditions: this.postconditions.slice()
        })
        this.methodName = ''
        this.methodVar = ''
        this.preconditionAf = null
        this.preconditionVr = null
        this.postconditionAf = null
        this.postconditionVr = null
        this.preconditions = []
        this.postconditions = []
        this.methodInvalid = false
      } else {
        this.methodInvalid = true
      }
    },
    deleteMethod (index) {
      this.problem.methods.splice(index, 1)
    }
  }
}
</script>
