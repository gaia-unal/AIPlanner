<template>
  <div>
    <p class="text-muted">Definición del problema</p>
    <div class="form-group row px-4">
      <div class="col-md-4">
        <label for="name">Nombre</label>
        <input
          id="name"
          type="text"
          class="form-control"
          v-model="problem.name"
          :class="{'invalid-input': initialInvalid}"
        >
      </div>
    </div>
    <h5>Estado inicial</h5>
    <div class="form-group row px-4">
      <div class="col-md-4">
        <label for="afInitial">Nombre afirmación</label>
        <input
          type="text"
          id="afInitial"
          class="form-control"
          v-model="initialAf"
          :class="{'invalid-input': initialInvalid}"
        >
      </div>
      <div class="col-md-4">
        <label for="varInitial">Variable</label>
        <input
          type="text"
          id="varInitial"
          class="form-control"
          v-model="initialVar"
          :class="{'invalid-input': initialInvalid}"
        >
      </div>
      <button class="btn btn-success col-md-1.5" style="margin-top: 32px" @click="addInitialState">Agregar</button>
    </div>
    <ul class="list-group my-3 px-4" v-if="problem.initialState.length > 0">
      <li class="list-group-item" v-for="(item, index) in problem.initialState" :key="item.id">
      <div class="form-group row" style="margin-bottom: 0px">
        <div class="col-md-4 my-auto">
          {{ item.name }}
        </div>
        <div class="col-md-4 my-auto">
          {{ item.value }}
        </div>
        <button class="btn btn-outline-danger col-md-1.5" style="margin-left: 8px" @click="deleteInitialItem(index)">Eliminar</button>
      </div>
      </li>
    </ul>
    <h5>Estado final</h5>
    <div class="form-group row px-4">
      <div class="col-md-4">
        <label for="afFinal">Nombre afirmación</label>
        <input
          type="text"
          id="afFinal"
          class="form-control"
          v-model="finalAf"
          :class="{'invalid-input': finalInvalid}"
        >
      </div>
      <div class="col-md-4">
        <label for="varFinal">Variable</label>
        <input
          type="text"
          id="varFinal"
          class="form-control"
          v-model="finalVar"
          :class="{'invalid-input': finalInvalid}"
        >
      </div>
      <button class="btn btn-success col-md-1.5" style="margin-top: 32px" @click="addfinalState">Agregar</button>
    </div>
    <ul class="list-group my-3 px-4" v-if="problem.finalState.length > 0">
      <li class="list-group-item" v-for="(item, index) in problem.finalState" :key="item.id">
      <div class="form-group row" style="margin-bottom: 0px">
        <div class="col-md-4 my-auto">
          {{ item.name }}
        </div>
        <div class="col-md-4 my-auto">
          {{ item.value }}
        </div>
        <button class="btn btn-outline-danger col-md-1.5" style="margin-left: 8px" @click="deleteFinalItem(index)">Eliminar</button>
      </div>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  props: ['problem'],
  data () {
    return {
      initialInvalid: false,
      finalInvalid: false,
      initialAf: '',
      initialVar: '',
      finalAf: '',
      finalVar: ''
    }
  },
  methods: {
    addInitialState () {
      if (this.initialAf.length > 0 && this.initialVar.length > 0 && this.problem.name.length > 0) {
        this.initialInvalid = false
        this.problem.initialState.push({
          name: this.initialAf,
          value: this.initialVar
        })
        this.initialAf = ''
        this.initialVar = ''
      } else {
        this.initialInvalid = true
      }
    },
    deleteInitialItem (index) {
      this.problem.initialState.splice(index, 1)
    },
    addfinalState () {
      if (this.finalAf.length > 0 && this.finalVar.length > 0 && this.problem.name.length > 0) {
        this.finalInvalid = false
        this.problem.finalState.push({
          name: this.finalAf,
          value: this.finalVar
        })
        this.finalAf = ''
        this.finalVar = ''
      } else {
        this.finalInvalid = true
      }
    },
    deleteFinalItem (index) {
      this.problem.finalState.splice(index, 1)
    }
  }
}
</script>
