const ctx = document.getElementById('temperature-chart');
const serverDataRoot = document.getElementById("__METEO_DATA__")
console.log(serverDataRoot.innerHTML)
const parsedServerData = JSON.parse(serverDataRoot.innerText)
console.log(parsedServerData)

const labels = ["Hola", "hola", "Hola", "hola", "Hola", "hola",]
const data = {
    labels: labels,
    datasets: [
        {
            label: 'Dataset 1',
            data: [1, 2, 3, 4, 5],
            borderColor: "rgba(255, 0, 0, 1)",
            backgroundColor: "rgba(255, 0, 0, 1)",
            yAxisID: 'y',
        },
        {
            label: 'Dataset 1',
            data: [5, 4, 2, 5, 4],
            borderColor: "rgba(255, 0, 0, 1)",
            backgroundColor: "rgba(255, 0, 0, 1)",
            yAxisID: 'y',
        },
    ]
};
// </block:setup>

// <block:config:0>
const config = {
    type: 'line',
    data: data,
    options: {
        responsive: true,
        interaction: {
            mode: 'index',
            intersect: false,
        },
        stacked: false,
        plugins: {
            title: {
                display: true,
                text: 'Chart.js Line Chart - Multi Axis'
            }
        },
        scales: {
            y: {
                type: 'linear',
                display: true,
                position: 'left',
            },
            y1: {
                type: 'linear',
                display: true,
                position: 'right',

                // grid line settings
                grid: {
                    drawOnChartArea: false, // only want the grid lines for one axis to show up
                },
            },
        }
    },
};


new Chart(ctx, config);