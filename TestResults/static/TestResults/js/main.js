const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const submitBtn = document.querySelector(".btn")

function displayResult(dataObject) {
    document.querySelector(".results-display").innerHTML = 
    `
    <table class="table table-bordered">
    <tr>
        <td>
            <b>Time of flight:</b>
            ${dataObject["Time"]} [sec]
        </td>
        <td>
            <b>Range:</b>
        ${dataObject["MaxRange"]} [m]
        </td>
        <td>
            <b>Max. Height:</b>
            ${dataObject["MaxHeight"]} [m]
        </td>
    </tr>
</table>
    `
}

    submitBtn.addEventListener("click", () => {
        const inputData = {
            "height": document.getElementById("height").value,
            "velocity": document.getElementById("velocity").value,
            "angle": document.getElementById("angle").value,
        }
        console.log(inputData);

        fetch("../api/submit",{
        method: 'POST',
        mode: 'same-origin',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(inputData)
    })
    .then(resp => resp.json())
    .then(data => displayResult(data))
    // .then(data => console.log(data))
    .catch(err => console.log("Error using fetch",err))

})

var ctx = document.getElementById('graph-area').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});