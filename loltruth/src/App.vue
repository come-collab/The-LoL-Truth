<template>
  <div id="app">
    <PlanetChart/>
  </div>
</template>

<script>
import PlanetChart from './components/PlanetChart.vue'

export default {
  name: 'App',
  components: {
    PlanetChart
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
