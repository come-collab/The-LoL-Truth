<template>
  <div>
    <canvas id="planet-chart2"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto'
import planetChartData2 from '../planet-data2.js'
export default {
  name: 'PlanetChart2',
    data() {
    return {
      planetChartData2: planetChartData2
    }
  },
  mounted() {
    const ctx = document.getElementById('planet-chart2');
    new Chart(ctx, this.planetChartData2);
  }
}
</script>