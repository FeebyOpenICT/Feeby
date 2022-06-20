export default function authorization({ store, error, route }) {
  // get permitted roles  from route
  const roles = route.meta.map((meta) => {
    if (meta.roles && Array.isArray(meta.roles)) {
      return meta.roles
    }
    return 0
  })[0]

  if (getArraysIntersection(store.getters['auth/roles'], roles).length == 0) {
    // user does not have one of the required roles
    error({ statusCode: 401, message: 'U heeft niet voldoende rechten om de opgevraagde gegevens te bekijken.', title: 'Not authorized'})
  }
}

function getArraysIntersection(a1,a2){
  return  a1.filter(function(n) { return a2.indexOf(n) !== -1;});
}
