<template>
  <div>
    <HeaderCom />
    <addButton />
    <CardCom />
  </div>
</template>

<script>
import CardCom from './CardCom.vue'

export default {
  name: 'HomePage',
  components: { CardCom }
}
</script>
