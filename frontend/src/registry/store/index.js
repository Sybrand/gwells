import Vue from 'vue'
import Vuex from 'vuex'
import ApiService from '@/common/services/gwells'
import { FETCH_DRILLER_LIST } from './actions.types.js'
import { SET_DRILLER_LIST, SET_LOADING, SET_LIST_ERROR } from './mutations.types.js'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    currentUser: 'anonymous',
    loading: false,
    listError: null,
    drillerList: []
  },
  mutations: {
    [SET_LOADING] (state, payload) {
      state.loading = payload
    },
    [SET_LIST_ERROR] (state, payload) {
      state.listError = payload
    },
    [SET_DRILLER_LIST] (state, payload) {
      state.drillerList = payload
    }
  },
  actions: {
    [FETCH_DRILLER_LIST] ({commit}, params) {
      commit(SET_LOADING, true)
      ApiService.query('drillers', params)
        .then((response) => {
          // const drillers = []
          // response.data.results.forEach((driller) => {
          //   const company = driller.companies.length ? driller.companies[0] : {}
          //   const companyName = company.organization_name || ''
          //   // const address = company.length ? company.street_address
          //   const tel = company.contact_tel || ''
          //   const email = company.contact_email || ''
          //   const status = driller.applications[0].registrations[0].status
          //   const details = {
          //     name: `${driller.first_name} ${driller.surname}`,
          //     company: companyName,
          //     tel: tel,
          //     email: email,
          //     status: status
          //   }
          //   drillers.push(details)
          // })
          commit(SET_LOADING, false)
          commit(SET_LIST_ERROR, null)
          commit(SET_DRILLER_LIST, response.data)
        })
        .catch((error) => {
          commit(SET_LOADING, false)
          commit(SET_LIST_ERROR, error.response)
        })
    }
  },
  getters: {
    loading (state) {
      return state.loading
    },
    listError (state) {
      return state.listError
    },
    drillers (state) {
      return state.drillerList
    }
  }
})
