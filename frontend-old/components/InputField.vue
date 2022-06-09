<template>
  <div id="productTextContainer" class="container">
    <h1 class="textBoxTitle">
      Toelichting
    </h1>
    <v-hover />
    <v-textarea
      id="postDescription"
      class="textField"
      counter
      :rules="rules"
      :value="value"
      type="text"
      placeholder="Schrijf hier je toelichting over je product..."
    />

    </v-hover>
      <v-textarea class="textField"
                  id="postDescription"
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
    rules: [v => v.length <= 25 || 'Characterlimiet overscheden'],
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
