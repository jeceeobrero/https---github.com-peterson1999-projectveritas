function loadJson(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}
  
function getData (){
    var data = loadJson('#jsonData');
    const mx = Object.values(data['month_dates']);
    const my = Object.values(data['month_values']);
    const dx = Object.values(data['day_dates']);
    const dy = Object.values(data['day_values']);
    const yx = Object.values(data['year_dates']);
    const yy = Object.values(data['year_values']);

    return [dx,dy,mx,my,yx,yy];
}


let context = getData();
console.log(context);
const dx = context[0];
const dy = context[1];
const mx = context[2];
const my = context[3];
const yx = context[4];
const yy = context[5];

const dates_array = [
    dx,
    mx,
    yx
]
const dates = [...dates_array];

const data_array = [
    dy,
    my,
    yy
]

const metricsdata = [
    {
        label: "Overall Credibility",
        data: data_array[0],
        fill: false,
        lineTension: 0,
        borderColor: "#4964FF",
        fill: false
    },  
]

const data = {
    labels: dates_array[0],
    datasets: metricsdata,
};

// config 
const config = {
    type: 'line',
    data,
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
        maintainAspectRatio: false,
    },
};

// render init block
const myChart = new Chart(document.getElementById('myChart'),config);

function filterData(){
    console.log("hello");
    const metricval = document.getElementById('metric');
    console.log(metricval.value);
    indexmetric = 0;
    switch(metricval.value){
        case 'Day': indexmetric = 0; break;
        case 'Month': indexmetric = 1; break;
        case 'Year': indexmetric = 2; break;
    }
    
    const dates2 = dates_array.map(dates_array => ([...dates_array]));
    const indexdate = [...dates2[indexmetric]];
    // console.log("dates2[0] "+dates2[0]);
    // console.log("dates2[1]"+dates2[1]);
    // console.log("dates2[2]"+dates2[2]);
    // console.log(indexdate);

    const startdate = String(document.getElementById('startdate').value);
    const enddate = String(document.getElementById('enddate').value);
    
    // console.log(dates2);
    // console.log("start "+ startdate);
    // console.log("end "+ enddate);

    let indexstartdate = 0;
    let indexenddate = 0;
    
    for (let i = 0; i < indexdate.length; i++) {
        if(String(indexdate[i]) >= startdate){
            indexstartdate=i;
            break;
        }
    }

    for (let i = 0; i < indexdate.length; i++) {
        console.log(String(indexdate[i]));
        if(String(indexdate[i]) <= enddate){
            indexenddate=i;   
        }
    }
    
    console.log("indexstart "+ indexstartdate);
    console.log("indexend "+ indexenddate);

    dates2[indexmetric] = dates2[indexmetric].slice(indexstartdate, indexenddate+1);
    myChart.config.data.labels = dates2[indexmetric];
    console.log(dates_array);
    myChart.update();

    let filteredData = [...data_array];
    console.log(filteredData);
    filteredData[indexmetric] = filteredData[indexmetric].slice(indexstartdate, indexenddate+1);
    
    let newdataset = [...metricsdata];
    console.log(newdataset);
    newdataset[0].data = filteredData[indexmetric];
    console.log(newdataset[0].data);

    console.log("filtered", filteredData[indexmetric]);
    myChart.config.data.datasets = newdataset;
    console.log(myChart.config.data.datasets);
    // console.log(myChart.config.data.datasets.data);
    myChart.update();
}