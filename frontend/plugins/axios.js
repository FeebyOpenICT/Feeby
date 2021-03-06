export default function ({ store, app: { $axios }, redirect }) {
  $axios.onRequest((config) => {
    // check if the user is authenticated
    if (store.getters['auth/isAuthenticated']) {
      // set the Authorization header using the access token
      config.headers.Authorization = 'Bearer ' + store.state.auth.token
    }
    if (process.client) {
      config.baseURL = '/api/v1'
    }

    return config
  })

  $axios.onError(async (error) => {
    const statusCode = error.response ? error.response.status : -1

    // auto refreshing of tokens
    if (statusCode === 401) {
      try {
        await store.dispatch('auth/refresh')
        return Promise.resolve($axios(config))
      } catch (e) {
        store.commit('auth/logout')
        return redirect('/unauthenticated')
      }
    }
    return Promise.reject(error)
  })
}
