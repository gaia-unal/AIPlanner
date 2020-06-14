import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    name: null,
    token: null,
    problems: {
      strip: {},
      htn: {}
    },
    currentProblem: null,
    authError: null,
    headError: null
  },
  mutations: {
    authUser (state, userData) {
      state.token = userData.token
      state.name = userData.name
    },
    authError (state, errorData) {
      state.authError = errorData
    },
    headError (state, errorData) {
      state.headError = errorData
    },
    setProblems (state, problems) {
      state.problems = problems
    },
    clearAuthData (state) {
      state.name = null
      state.token = null
      state.problems = {
        strip: {},
        htn: {}
      }
      state.currentProblem = {}
      state.authError = null
      state.headError = null
    },
    clearError (state) {
      state.headError = null
      state.authError = null
    },
    setProblem (state, problem) {
      state.currentProblem = problem
    }
  },
  actions: {
    signup ({ commit }, authData) {
      Vue.http.post('http://localhost:8000/auth/sign-up', authData)
        .then(response => {
          const data = response.body
          // console.log(data)
          commit('authUser', {
            token: data.token,
            name: data.name
          })
          localStorage.setItem('token', data.token)
          localStorage.setItem('name', data.name)
          router.push('/')
        }, error => {
          commit('authError', error.body)
          // console.log(error.body)
        })
    },
    login ({ commit }, authData) {
      Vue.http.post('http://localhost:8000/auth/login', authData)
        .then(response => {
          const data = response.body
          // console.log(data)
          commit('authUser', {
            token: data.token,
            name: data.name
          })
          localStorage.setItem('token', data.token)
          localStorage.setItem('name', data.name)
          router.push('/')
        }, error => {
          // console.log(error.body)
          commit('authError', error.body)
        })
    },
    changeData ({ commit, state }, userData) {
      commit('clearError')
      Vue.http.put('http://localhost:8000/user', userData, {
        headers: {
          'Authorization': 'Bearer ' + state.token
        }
      })
        .then(response => {
          // console.log(response.body)
        }, error => {
          // console.log(error)
          commit('headError', error.body)
        })
    },
    autoLogin ({ commit }) {
      const token = localStorage.getItem('token')
      const name = localStorage.getItem('name')
      if (token) {
        commit('authUser', {
          token: token,
          name: name
        })
      }
    },
    logout ({ commit }, route) {
      commit('clearAuthData')
      localStorage.removeItem('token')
      if (route !== '/') {
        router.push('/')
      }
    },
    sendStripProblem ({ state }, userData) {
      Vue.http.post('http://localhost:8000/user/strip/problem', userData, {
        headers: {
          'Authorization': 'Bearer ' + state.token
        }
      })
        .then(response => {
          // console.log(response.body.message)
          userData.output = response.body.message
        }, error => {
          // console.log(error)
        })
    },
    sendHtnProblem ({ state }, userData) {
      Vue.http.post('http://localhost:8000/user/htn/problem', userData, {
        headers: {
          'Authorization': 'Bearer ' + state.token
        }
      })
        .then(response => {
          // console.log(response.body.message)
          userData.output = response.body.message
        }, error => {
          // console.log(error)
        })
    },
    getProblems ({ commit, state }) {
      Vue.http.get('http://localhost:8000/user/problems', {
        headers: {
          'Authorization': 'Bearer ' + state.token
        }
      })
        .then(response => {
          // console.log(response.body.message)
          commit('setProblems', response.body.message)
        }, error => {
          // console.log(error)
        })
    },
    deleteProblem ({ dispatch, state }, userData) {
      Vue.http.delete('http://localhost:8000/user/' + userData.type + '/problem/' + userData.key, {
        headers: {
          'Authorization': 'Bearer ' + state.token
        }
      })
        .then(response => {
          // console.log(response.body.message)
          dispatch('getProblems')
        }, error => {
          // console.log(error)
        })
    },
    clearError ({ commit }) {
      commit('clearError')
    },
    updateHeadError ({ commit }, error) {
      commit('headError', error)
    },
    setCurrentProblem ({ commit }, problem) {
      commit('setProblem', problem)
    }
  },
  getters: {
    isAuthenticated (state) {
      return state.token !== null
    },
    authError (state) {
      return state.authError
    },
    headError (state) {
      return state.headError
    },
    name (state) {
      return state.name
    },
    getProblems (state) {
      return state.problems
    },
    getCurrentProblem (state) {
      return state.currentProblem
    }
  }
})
