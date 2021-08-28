export const planetChartData = {
    type: 'doughnut',
    data : {
      labels: ['1 years','2 years','3 years','4 years','5 or More','Smurfs'],
      datasets: [{
        label: ['First rank ever reached by the player'],
        data: [342, 188, 97, 74, 16, 185],
        fill: false,
        backgroundColor: [
          'rgb(255, 99, 132, 0.5)',
          'rgb(75, 192, 192, 0.5)',
          'rgb(255, 205, 86, 0.5)',
          'rgb(201, 203, 207, 0.5)',
          'rgb(54, 162, 235, 0.5)',
          'rgb(30,144,255)'
        ],
        borderColor: [
          'rgb(255, 99, 132)',
          'rgb(75, 192, 192)',
          'rgb(255, 205, 86)',
          'rgb(201, 203, 207)',
          'rgb(54, 162, 235)',
          'rgb(30,144,255)'
        ],
        borderWidth: 1
      }]
    },
    options: {
    }
  };
    
  export default planetChartData;