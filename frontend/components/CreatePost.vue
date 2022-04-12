<template>
  <div id="page-container">
    <HeaderCom />
    <PostTitle />
    <div id="content-wrap" class="postPage">
      <h1 class="pageTitle">Product inleveren</h1>
      <InputField />
      <UploadBox />
      <AspectCommunication />
      <AspectKnowledge />

      <v-card v-for="post in posts" :key="post.id" class="cardsList">
        <div class="postContainer">
          <v-card-title>{{ post.title }}</v-card-title>
        </div>
      </v-card>
    </div>
    <footer id="footer" />
  </div>
</template>

<script>
import { axiosInstance } from "../lib/axiosInstance";
import HeaderCom from "./HeaderCom.vue";
import "~/.css/styles.css";
export default {
  name: "CreatePost",
  components: { HeaderCom },
  data() {
    return {
      form: {
        title: "",
        description: "",
        aspects: "",
      },
    };
  },
  methods: {
    submitForm() {
      axiosInstance
        .post("api/v1/posts", this.form)
        .then((response) => (this.form = response.data))
        .catch(function (error) {
          if (error.response) {
            // De post request is gemaakt en de server gaf in de terminal een status code aan

            console.log(error.response.data);
            console.log("render error", error.response.status);
            console.log(
              "je bent momenteel niet ingelogd",
              error.response.headers
            );
          } else if (error.request) {
            // Request is verzonden, echter geen reactie terug
            console.log("Er is iets fout gegaan", error.request);
          } else {
            // Iets in de request heeft voor een error gezorgd
            console.log(
              "Er is iets mis gegaan met het versturen van de data",
              error.message
            );
          }
          console.log(error.config);
        });
    },
  },
};
</script>
