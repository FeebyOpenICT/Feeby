<template>
  <div class="container" id="productTextContainer">
    <h1 class="textBoxTitle">
      Toelichting
    </h1>
    <v-hover>

    </v-hover>
      <v-textarea class="textField"
                  id="postDescription"
                  counter
                  :rules="rules"
                  :value="value"
                  type="text"
                  placeholder="Schrijf hier je toelichting over je product..."
      />

    <div id="characterLimit">max. 1000 characters</div>
  </div>
</template>

<!--Runs script for maximum character limit in Checkbox-->
<script type="text/javascript">
export default {
  data: () => ({
    rules: [v => v.length <= 1000 || 'Characterlimiet overscheden'],
    value: ''
  })
}
</script>
<style>
@import '.css/styles.css';
#characterLimit{
  float: right;

}
</style>
