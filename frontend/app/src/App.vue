<template>
  <div id="app">
    <HeaderComponent/>
    <router-view/>
  </div>
</template>

<script>

import HeaderComponent from './components/HeaderComponent.vue';
export default {
  name: "app",
  components: {
    HeaderComponent,
  }
}

</script>

<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #7c848b;
    background: rgb(245, 245, 250);
  }

  button {
      color: #fff;
      border: none;
      padding: 5px 9px;
      margin: 0px 3px;
      border-radius: 10%;
      cursor: pointer;
  }

</style>
