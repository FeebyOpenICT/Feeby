export const state = () => ({
  token: null,
})

export const getters = {
  isAuthenticated: (state) => {
    return !!state.token
  },
  userId: (state) => {
    return state.user.id
  },
}

export const mutations = {
  setTokens(state, token) {
    state.token = token
  },
  setUser(state, user) {
    state.user = user
  },
  logout(state) {
    state.token = null
    state.user = null
  },
}

export const actions = {
  async login({ commit, dispatch }, token) {
    commit('setTokens', token)
    await dispatch('getUser')
  },
  async getUser({ commit }) {
    const res = await this.$axios.$get('/users/self')
    commit('setUser', res)
  },
  async refresh({ commit }) {
    const res = await this.$axios.$post('/auth/refresh')
    commit('setTokens', res)
  },
}
