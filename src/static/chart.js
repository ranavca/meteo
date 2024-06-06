const ctx = document.getElementById('temperature-chart');
const serverDataRoot = document.getElementById("__METEO_DATA__")
const parsedServerData = JSON.parse(serverDataRoot.innerText).data
const lastTen = parsedServerData.slice(-50)


const labels = lastTen.map((item) => item[1])
const temperature = lastTen.map((item) => item[2])
const humidity = lastTen.map((item) => item[3])
const pressure = lastTen.map((item) => item[4])
const data = {
    labels: labels,
    datasets: [
        {
            label: 'Temperatura',
            data: temperature,
            borderColor: "rgba(255, 0, 0, 1)",
            backgroundColor: "rgba(255, 0, 0, 1)",
            yAxisID: 'y',
        },
        {
            label: 'Presión',
            data: pressure,
            borderColor: "rgba(0, 255, 0, 1)",
            backgroundColor: "rgba(0, 255, 0, 1)",
            yAxisID: 'y',
        },
        {
            label: 'Humedad',
            data: humidity,
            borderColor: "rgba(0, 0, 255, 1)",
            backgroundColor: "rgba(0, 0, 255, 1)",
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
                text: 'Últimos datos'
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