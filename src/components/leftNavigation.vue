
<template>
  <v-navigation-drawer app light permanent width="250">
    <img src="../assets/peachlogo.png" height="200px" width="200px">
    <v-list>
      <v-list-tile v-for="item in items" :key="item.title" v-on:click>
        <!--
        <v-list-tile-action>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-tile-action>
        -->
        <v-list-tile-content align-center>
          <v-list-tile-title align-center>{{ item.title }}</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>
<script>
export default {
  data() {
    return {
      items: [
        {
          title: "featured",
          icon: "star"
        },
        {
          title: "clothing",
          icon: "star"
        },
        { title: "shoes", icon: "star" },
        { title: "phones", icon: "star" },
        { title: "electronics", icon: "star" }
      ]
    };
  }
};
</script>