import cookie from 'cookie'

export const actions = {
  async nuxtServerInit({ dispatch }, { req }) {
    if (req.headers.cookie) {
      const { jwt } = cookie.parse(req.headers.cookie)
      if (jwt) {
        await dispatch('auth/login', jwt)
      }
    }
  },
}
