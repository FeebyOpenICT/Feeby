<script src="https://cdnjs.cloudflare.com/ajax/libs/vue/1.0.18/vue.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue@2.5.13/dist/vue.js"></script>

<template>
  <div class="checkBoxContainer" id="knowledge">
    <div id="aspectCheck">
      <v-checkbox type="button" class="selectBox" @click="isHidden = !isHidden"></v-checkbox>
      <p class="aspect" style="color: white;"><strong>Juiste kennis opdoen</strong></p>
    </div>
      <v-textarea class="textField"
        id="aspectDescription"
        v-if="!isHidden"
        counter
        type="text"
        placeholder="Schrijf hier je toelichting over dit aspect..."
      />
    </div>
</template>

<!--Makes textboxes appear upon activating or disabling checkboxes-->
<script type="text/javascript">
export default {
  name: 'SelectAspects',
  data: () => ({
    visible: true,
    isHidden: true
  })
}
</script>

<style>
@import '../../.css/styles.css';
</style>
