<template ref="upload" lazy-validation>
    <v-card v-model="e1"
      @drop.prevent="dragover = false"
      @dragover.prevent="dragover = true"
      @dragenter.prevent="dragover = true"
      @dragleave.prevent="dragover = false"
      style="background-color: #0079CF"
    >
      <v-card-text
        v-model="valid"
        >
        <v-row class="d-flex flex-column" dense align="center" justify="center">
          <v-icon class="mt-3" size="70" style="color:white">mdi-cloud-upload</v-icon>
          <p class="d-flex flex-column" dense align="center" justify="center" style="color: white">
            Sleep je bestanden vanaf jou computer hierin.
          </p>
        </v-row>
        <v-file-input
          multiple
          show-size
          truncate-length="15"
        />
      </v-card-text>
      <v-card-actions></v-card-actions>
      <v-spacer></v-spacer>
      <div className="buttons">
        <v-btn class="btn"
               @click="e1=1"
               style="background-color: #0079CF; color: white"
        >
          Ga terug
        </v-btn>
        <v-btn class="btn"
               color="primary"
               @click="e1 = 4"
               :disabled="!valid"
               style="background-color: #0079CF; color: white"
        >
          Ga verder
        </v-btn>
      </div>
    </v-card>
</template>

<script>
import { axiosInstance } from '~/lib/axiosInstance'

export default {
  name: 'UploadBox',
  data () {
    return {
      e1: 1,
      user: '',
      dragover: false,
      uploadedFiles: [],
      input: {
        uploadFiles: ''
      }
    }
  },
  mounted () {
    axiosInstance
      .post('api/v1/users/1/posts', this.input)
      .then(response => (this.input = response.data))
  },

  onDrop (e) {
    this.dragover = false
    if (!this.multiple && e.dataTransfer.files.length > 1) {
      this.$store.dispatch('addNotification', {
        message: 'Only one file can be uploaded at a time..',
        colour: 'error'
      })
    } else {
      e.dataTransfer.files.forEach(element =>
        this.uploadedFiles.push(element)
      )
    }
  }
}
</script>

<style scoped>

</style>
