<template>
  <form>
    <div id="productTextContainer" class="container">
      <h1 class="textBoxTitle">
        Titel
      </h1>
      <v-hover />
      <v-textarea
        id="aspectTitel"
        class="textField"
        counter
        :max-length="255"
        :value="Title"
        type="text"
        placeholder="Schrijf hier je Titel van je aspect..."
      />

      <div id="characterLimit">
        max. 255 characters
      </div>
    </div>
    <div id="productTextContainer" class="container">
      <h1 class="textBoxTitle">
        Beschrijving
      </h1>
      <v-hover />
      <v-textarea
        id="aspectBeschrijving"
        class="textField"
        counter
        :max-length="1000"
        :value="Description"
        type="text"
        placeholder="Schrijf hier je beschrijving over dit aspect..."
      />

      <div id="characterLimit">
        max. 1000 characters
      </div>
    </div>
    <div id="productTextContainer" class="container">
      <h1 class="textBoxTitle">
        Korte Beschrijving
      </h1>
      <v-hover />
      <v-textarea
        id="aspectKorteBeschrijving"
        class="textField"
        counter
        :max-length="255"
        :value="ShortDescription"
        type="text"
        placeholder="Schrijf hier je korte beschrijving over dit aspect..."
      />

      <div id="characterLimit">
        max. 255 characters
      </div>
    </div>
    <div id="productTextContainer" class="container">
      <h1 class="textBoxTitle">
        Link
      </h1>
      <v-hover />
      <v-textarea
        id="aspectLink"
        class="textField"
        counter
        :max-length="2000"
        :value="Link"
        type="text"
        placeholder="Schrijf hier je externe link van je aspect..."
      />

      <div id="characterLimit">
        max. 2000 characters
      </div>
    </div>
    <div id="productTextContainer" class="container">
      <h1 class="textBoxTitle">
        Aspect Rating
      </h1>
      <v-hover />
      <v-list class="aspectRatingsBox">
        <v-list-item-group>
          <v-list-item
            v-for="value in values"
            :key="value"
          >
            <v-list-item-content>
              <v-list-item-title v-text="value.rating" />
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </div>
  </form>
</template>
<script>
import { axiosInstance } from '../../lib/axiosInstance'
export default {
  name: 'AspectAanmaken',
  reqpost: axiosInstance.post('/api/v1/aspects/'),
  reqget: axiosInstance.get('/api/v1/ratings/'),
  data () {
    return {
      values: null
    }
  },
  mounted () {
    axiosInstance
      .request([this.reqpost, this.reqget])
      .then(response => (this.values = response.data))
      .catch(error => console.log(error))
  }
}
</script>
<style scoped>
@import '.css/styles.css';
#characterLimit{
  float: right;

}
</style>
