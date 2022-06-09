<template>
  <div>Only admins, content-developers and Instructors can view this page</div>
</template>

<script>
export default {
  middleware: ['authenticated', 'authorization'],
  meta: {
    roles: ['admin', 'content_developer', 'instructor']
  }
}
</script>
