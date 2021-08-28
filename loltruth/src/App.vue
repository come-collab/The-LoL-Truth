<template>
  <div id="app">
    <MainText/>
    <PlanetChart/>
    <SecondGraphText/>
    <PlanetChart2/>
  </div>
</template>

<script>
import PlanetChart from './components/PlanetChart.vue'
import PlanetChart2 from './components/PlanetChart2.vue'
import MainText from './components/MainText.vue'
import SecondGraphText from './components/SecondGraphText.vue'

export default {
  name: 'App',
  components: {
    PlanetChart,
    PlanetChart2,
    MainText,
    SecondGraphText
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
  margin-right : 15%;
  margin-left : 15%;
}
p { font-family: Quicksand; font-size: 14px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 20px; }
h3 { font-family: Quicksand; font-size: 14px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 15.4px; }
h1 { font-family: Quicksand; font-size: 24px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 26.4px; }
</style>
