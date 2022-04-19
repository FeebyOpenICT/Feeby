<template>
  <div>
    <HeaderCom />
    <addButton />
    <CardCom />
    <FooterCom />
  </div>
</template>

<script>
import CardCom from "./CardCom.vue";
import FooterCom from "./FooterCom.vue";

export default {
  name: "HomePage",
  components: { CardCom, FooterCom },
};
</script>
