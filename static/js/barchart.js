// Initiate variables
var index = 1;
var scores;

// Fetch chart values from application.py and make chart for each score
fetch('/chart_values')
    .then((response) => {
    return response.json();
    })
    .then((data) => {
    scores = data;
    scores.forEach(score => make_chart(score));
    });

// Make chart with scores obtained from fetch
function make_chart(score) {
    var ctx = document.getElementById('myChart'+index);
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: score[1],
            datasets: [{
                data: score[0],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                ],
                borderWidth: 6
            }]
        },
        options: {
            legend: {
                display: false
            },
            title: {
                display: true,
                text: score[2]
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        stepSize: 1
                    }
                }]
            }
        }
    });
    index++;
}