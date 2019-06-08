<template>
  <v-app>
    <nav class="navbar">
      <v-toolbar app flat blue>
        <v-toolbar-title class="headline text-uppercase">
          <span>Canadian</span>
          <span class="font-weight-light">Discount</span>
        </v-toolbar-title>
        <v-flex xs5 offset-xs2>
          <v-text-field placeholder="Search Product" solo>
            <v-btn icon>
              <v-icon>search</v-icon>
            </v-btn>
          </v-text-field>
        </v-flex>
      </v-toolbar>
    </nav>
    <left-nav></left-nav>
    <v-container fluid ma-3 mt-0>
      <v-content>
        <show-products></show-products>
      </v-content>
    </v-container>
  </v-app>
</template>

<script>
import showProducts from "./components/showProducts.vue";
import leftNavigation from "./components/leftNavigation.vue";

export default {
  name: "App",
  components: {
    "show-products": showProducts,
    "left-nav": leftNavigation
  },
  data() {
    return {
      //
    };
  }
};
</script>

<style>
#searchbar {
  margin: 0 auto;
  width: 30%;
  background: white;
}
</style>
