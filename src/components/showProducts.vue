<template>
  <div id="showProducts" class="layout column justify-center">
    <h1>Featured Products</h1>
    <v-layout row wrap>
      <v-card class="singleProduct" hover v-for="product in products" v-bind:key="product.id">
        <v-card-title primary-title>
          <v-flex xs2>
            <img src="../assets/UNIQLO_logo.svg" height="50px" width="50px">
          </v-flex>
          <v-flex xs8>
            <div>
              <h3 class="subheading mb-0">{{product.topic | shortenTitle}}</h3>
              <h4 class="caption">#{{brand}} #{{item}}</h4>
            </div>
          </v-flex>
          <v-flex ml-2 xs1>
            <div>
              <button text-align="center" v-on:click.self="upvote">upvote ({{upvotes}})</button>
            </div>
          </v-flex>
        </v-card-title>
        <div class="pb-3 text_test">
          <v-card-text>{{product.title | shortenText}} ...</v-card-text>
        </div>
        <v-card-actions>
          <v-btn flat color="orange" class="text-lowercase">Deal Link</v-btn>
          <v-btn flat color="orange" class="text-lowercase">Read More</v-btn>
        </v-card-actions>
      </v-card>
    </v-layout>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      products: null,
      upvotes: 0,
      brand: "",
      item: ""
    };
  },
  methods: {
    generateRandomBrand: function() {
      let brands = ["adidas", "nike", "patagucci", "bryan"];
      this.brand = brands[Math.floor(Math.random() * brands.length)];
      return this.brand;
    },
    generateRandomItem: function() {
      let items = ["shoes", "watch", "pants", "outerwear"];
      this.item = items[Math.floor(Math.random() * items.length)];
      return this.item;
    },
    upvote: function() {
      this.upvotes++;
    }
  },
  created() {
    test: {
      axios
        .get("http://127.0.0.1:8080/threads/featured")
        .then(response => (this.products = response.data.threads));
    }
    generateRandom: {
      this.generateRandomBrand();
      this.generateRandomItem();
    }
  },

  filters: {
    shortenTitle: function(value) {
      return value.slice(0, 30);
    },

    shortenText: function(value) {
      return value.slice(0,150);
    }
  }
};
</script>

<style scoped>
#showProducts {
  width: 100%;
}

#showProducts h1 {
  padding-bottom: 20px;
}

.text_test {
  height: 60px;
}

.singleProduct {
  width: 30%;
  margin-right: 10px;
  margin-bottom: 10px;
}
</style>