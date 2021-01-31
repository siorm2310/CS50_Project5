const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
const submitBtn = document.querySelector(".btn");
var ctx = document.getElementById("graph-area").getContext("2d");

function displayResult(dataObject) {
  document.querySelector(".results-display").innerHTML = `
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
    `;
}

function buildDataPoints(dataObject) {
    x = dataObject["x"]
    y = dataObject["y"]

    formattedPoints = x.map(function(element,idx){
      return {
        x : element,
        y : y[idx]
      }
    })

    return formattedPoints
}

function populateChart(serielizedDataObject) {
  var myChart = new Chart(ctx, {
    type: "line",

    data: {
      datasets: [
        {
          label: "Height Vs. distance [m]",
          data: serielizedDataObject,
        },
      ],
    },
    options: {
      scales: {
          xAxes: [{
              ticks: {
                beginsAtZero : true
              },
              type: 'linear',
              position: 'bottom',
              stacked: true,
              suggestedMax: 40
          }],
          yAxes :[{
            ticks: {
              beginsAtZero : true
            },
            type: 'linear',
            position: 'bottom',
            stacked: true,
            suggestedMax: 40
        }],
      }
  }
  });
}

  function generateResultsFront(dataObject){
    displayResult(dataObject)
    const formattedPoints = buildDataPoints(dataObject)
    populateChart(formattedPoints)
  }

submitBtn.addEventListener("click", () => {
  const inputData = {
    height: document.getElementById("height").value,
    velocity: document.getElementById("velocity").value,
    angle: document.getElementById("angle").value,
  };

  fetch("../api/submit", {
    method: "POST",
    mode: "same-origin",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(inputData),
  })
    .then((resp) => resp.json())
    .then((data) => generateResultsFront(data))
    .catch((err) => console.log("Error using fetch", err));
});
