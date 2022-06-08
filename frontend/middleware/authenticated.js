export default function authenticated({ store, redirect }) {
  if (!store.getters['auth/isAuthenticated']) {
    redirect('/unauthenticated')
  }
}
