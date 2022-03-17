<template>
  <v-container class="uploadContainer">
    <h1>Upload je bestanden</h1>
    <div class="upload">
      <v-file-input v-if="!isHidden"
                    chips
                    multiple
                    truncate-length="50"
      ></v-file-input>
    </div>
  </v-container>
</template>

<script type="text/javascript">
export default {
  name: 'UploadBox'
}
</script>

<style>
@import '.css/styles.css';
@import '.css/uploadBox.css';
</style>
