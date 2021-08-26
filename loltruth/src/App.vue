<template>
  <div id="app">
    <h1> League of legend truth based on data</h1>
    <p>This website have for goal to explain to people why League of Legend is top notch in terms of competition</p>
    <p>And why the dream of becoming a pro player/high rank player is extremely difficult to reach</p>
    <p>The whole website fetching of data, process of treating those data's and code is available on <a href = "https://github.com/come-collab">GitHub </a> </p>
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
