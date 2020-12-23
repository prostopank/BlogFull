import axios from 'axios'

export default ({
    namespaced: true,
    state: {
        token: '',
        user: null,
    },

    getters:{
        authenticated(state){
            return state.token && state.user
        },

        user(state){
            return state.user
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
            let responce = axios.post("/auth/token", credentials)
            dispatch('attempt', (await responce).data.token)
        },

        async attempt({ commit }, token) {
            commit('SET_TOKEN', token)

            try {
                let responce = await axios.get('auth/users/me/', {
                    headers:{
                        'Authorization': 'Token ' + token
                    }
                })
                commit('SET_USER', (await responce).data)
                axios.defaults.headers.common["X-XSRF-TOKEN"] = token
                axios.defaults.headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
            

            } catch (e) {
                commit('SET_TOKEN', null)
                commit('SET_USER', null)
            }
        }

    },

})