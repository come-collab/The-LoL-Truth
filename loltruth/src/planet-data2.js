export const planetChartData = {
    type: 'doughnut',
    data : {
      labels: ['1 years','2 years','3 years','4 years','5 or More','Smurfs'],
      datasets: [{
        axis: 'y',
        label: ['First rank ever reached by the player'],
        data: [84, 126, 185, 700],
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