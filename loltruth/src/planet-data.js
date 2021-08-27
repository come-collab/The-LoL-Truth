export const planetChartData = {
  type: 'bar',
  data : {
    labels: ['Silver','Gold','Platinum','Diamond'],
    datasets: [{
      axis: 'y',
      label: ['First rank ever reached by the player'],
      data: [65, 59, 80, 450],
      fill: false,
      backgroundColor: [
        'rgba(27,30,35, 0.2)',
        'rgba(255, 205, 86, 0.2)',
        'rgba(8, 69, 126, 0.4)',
        'rgba(75, 192, 192, 0.2)'
      ],
      borderColor: [
        'rgb(27, 10, 30',
        'rgb(255, 159, 64)',
        'rgb(8, 30, 126)',
        'rgb(75, 192, 192)'
      ],
      borderWidth: 1
    }]
  },
  options: {
    indexAxis: 'y',
  }
};
  
export default planetChartData;