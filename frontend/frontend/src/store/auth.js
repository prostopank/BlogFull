import axios from 'axios'


export default ({
    namespaced: true,
    state: {
        token: '',
        user: null,
    },

    getters: {
        authenticated(state) {
            return state.token && state.user
        },

        user(state) {
            return state.user
        },
        tokenn(state) {
            return state.token
        }
    },
    mutations: {
        SET_TOKEN(state, token) {
            state.token = token
        },
        SET_USER(state, data) {
            state.user = data
        }

    },
    actions: {
        async signIn({ dispatch }, credentials) {
            let responce = axios.post("http://localhost:8000/api/auth/token", credentials)
            return dispatch('attempt', (await responce).data.token)
        },

        async attempt({ commit, state }, token) {

            if (token) {
                commit('SET_TOKEN', token)
            }

            if (!state.token) {
                return
            }

            try {
                let responce = await axios.get('http://localhost:8000/api/auth/users/me/')
                commit('SET_USER', (await responce).data)



            } catch (e) {
                commit('SET_TOKEN', null)
                commit('SET_USER', null)
            }

        },

        signOut({commit}){
           // return axios.post('http://localhost:8000/api/auth/users/logout').then(()=>{
                commit('SET_TOKEN', null)
                commit('SET_USER', null)
           // })
        }

    },

})