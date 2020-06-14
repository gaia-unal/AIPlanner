<template>
  <div>
    <h5 class="">Agregar operadores</h5>
    <div class="border p-4">
      <div class="form-group row">
        <label class="col-md-4 my-auto" for="nameOperator">Nombre</label>
        <div class="col-md-4">
          <input
            type="text"
            id="nameOperator"
            class="form-control"
            v-model="operatorName"
            :class="{'invalid-input': operatorInvalid}"
            placeholder="nombre del operador"
            >
        </div>
      </div>
      <div class="form-group row">
        <label for="nameVarOperator" class="col-md-4 my-auto">Variables que recibe</label>
        <div class="col-md-4">
          <input
            type="text"
            id="nameVarOperator"
            class="form-control"
            v-model="operatorVar"
            :class="{'invalid-input': operatorInvalid}"
            placeholder="variable1, variable2, etc"
          >
        </div>
      </div>
      <div class="form-group row">
        <label for="preconditionOperator" class="col-md-4 my-auto">Qué se debe cumplir</label>
        <div class="col-md-2">
          <input
            type="text"
            id="preconditionOperator"
            class="form-control"
            v-model="preconditionAf"
            :class="{'invalid-input': operatorInvalid}"
            placeholder="nombre"
          >
        </div>
        <div class="col-md-2">
          <input
            type="text"
            class="form-control"
            v-model="preconditionVr"
            :class="{'invalid-input': operatorInvalid}"
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
        <label for="delete" class="col-md-4 my-auto">Qué se debe eliminar</label>
        <div class="col-md-2">
          <input
            type="text"
            id="delete"
            class="form-control"
            :class="{'invalid-input': operatorInvalid}"
            v-model="deleteAf"
            placeholder="nombre"
          >
        </div>
        <div class="col-md-2">
          <input
            type="text"
            class="form-control"
            :class="{'invalid-input': operatorInvalid}"
            v-model="deleteVr"
            placeholder="variables"
          >
        </div>
        <button class="btn btn-success col-md-1.5" @click="addDelete">Agregar</button>
      </div>
      <div class="form-group row">
        <div class="col-md-4"></div>
        <div class="col-md-6">
          <ul class="list-group" v-if="del.length > 0">
          <li class="list-group-item" v-for="(item, index) in del" :key="item.id">
            <div class="form-group row" style="margin-bottom: 0px">
              <div class="col-md-4 my-auto">
                {{ item.name }}
              </div>
              <div class="col-md-4 my-auto">
                {{ item.value }}
              </div>
              <button class="btn btn-outline-danger col-md-1.5" style="margin-left: 8px" @click="deleteDelItem(index)">Eliminar</button>
            </div>
          </li>
        </ul>
        </div>
      </div>
      <div class="form-group row">
        <label for="add" class="col-md-4 my-auto">Qué se debe agregar</label>
        <div class="col-md-2">
          <input
            type="text"
            id="add"
            class="form-control"
            :class="{'invalid-input': operatorInvalid}"
            v-model="addAf"
            placeholder="nombre"
          >
        </div>
        <div class="col-md-2">
          <input
            type="text"
            class="form-control"
            :class="{'invalid-input': operatorInvalid}"
            v-model="addVr"
            placeholder="variables"
          >
        </div>
        <button class="btn btn-success col-md-1.5" @click="addAdd">Agregar</button>
      </div>
      <div class="form-group row">
        <div class="col-md-4"></div>
        <div class="col-md-6">
          <ul class="list-group" v-if="add.length > 0">
          <li class="list-group-item" v-for="(item, index) in add" :key="item.id">
            <div class="form-group row" style="margin-bottom: 0px">
              <div class="col-md-4 my-auto">
                {{ item.name }}
              </div>
              <div class="col-md-4 my-auto">
                {{ item.value }}
              </div>
              <button class="btn btn-outline-danger col-md-1.5" style="margin-left: 8px" @click="deleteAddItem(index)">Eliminar</button>
            </div>
          </li>
        </ul>
        </div>
      </div>
      <div class="form-group row">
        <div class="col-md-12">
          <button class="btn btn-success float-right" @click="addOperator">Agregar método</button>
        </div>
      </div>
    </div>
    <div class="border p-4 mt-1" v-if="problem.operators.length > 0">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Nombre</th>
            <th scope="col">Variables</th>
            <th scope="col">Precondición</th>
            <th scope="col">Del</th>
            <th scope="col">Add</th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(operator, index) in problem.operators" :key="operator.id">
            <td class="align-middle">{{ operator.name }}</td>
            <td class="align-middle">{{ operator.variables }}</td>
            <td class="align-middle">
              <p class="mb-0" v-for="item in operator.preconditions" :key="item.id">{{ item.name }}{{ item.value }}</p></td>
            <td class="align-middle">
              <p class="mb-0" v-for="item in operator.del" :key="item.id">{{ item.name }}{{ item.value }}</p>
            </td>
            <td class="align-middle">
              <p class="mb-0" v-for="item in operator.add" :key="item.id">{{ item.name }}{{ item.value }}</p>
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
      del: [],
      deleteAf: null,
      deleteVr: null,
      add: [],
      addAf: null,
      addVr: null,
      operatorName: '',
      operatorVar: '',
      operatorInvalid: false
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
    addDelete () {
      if (this.deleteAf.length > 0 && this.deleteVr.length > 0) {
        this.del.push({
          name: this.deleteAf,
          value: this.deleteVr.split(',')
        })
      }
    },
    deleteDelItem (index) {
      this.del.splice(index, 1)
    },
    addAdd () {
      if (this.addAf.length > 0 && this.addVr.length > 0) {
        this.add.push({
          name: this.addAf,
          value: this.addVr.split(',')
        })
      }
    },
    deleteAddItem (index) {
      this.add.splice(index, 1)
    },
    addOperator () {
      if (this.operatorName.length > 0 && this.operatorVar.length > 0 && this.add.length > 0) {
        this.problem.operators.push({
          name: this.operatorName,
          variables: this.operatorVar.split(','),
          preconditions: this.preconditions.slice(),
          del: this.del.slice(),
          add: this.add.slice()
        })
        this.operatorName = ''
        this.operatorVar = ''
        this.preconditionAf = null
        this.preconditionVr = null
        this.deleteAf = null
        this.deleteVr = null
        this.preconditions = []
        this.del = []
        this.add = []
        this.addAf = null
        this.addVr = null
        this.operatorInvalid = false
      } else {
        this.operatorInvalid = true
      }
    },
    deleteMethod (index) {
      this.problem.operators.splice(index, 1)
    }
  }
}
</script>
