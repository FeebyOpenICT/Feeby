export default function authenticated({ store, error }) {
  if (!store.getters['auth/isAuthenticated']) {
    error({ statusCode: 403, message: 'U bent niet ingelogd bij Feeby. Verwijder uw cookies en ga terug naar de canvas omgeving.', title: 'Not authenticated'})
  }
}
