<template>
  <div id="app">
    <MainText/>
    <PlanetChart/>
  </div>
</template>

<script>
import PlanetChart from './components/PlanetChart.vue'
import MainText from './components/MainText.vue'

export default {
  name: 'App',
  components: {
    PlanetChart,
    MainText
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
