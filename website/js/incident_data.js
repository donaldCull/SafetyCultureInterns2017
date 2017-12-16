var raw_data;
var incident_names = [];
var incident_count = [];

window.onload = function start() {
    // runs the following functions when the pages load
    get_incident_details(function () {
        create_visualisation();
        document.getElementById("myChart").style.visibility = "visible";
    });

};


function get_incident_details(callback) {
    // connects to server to get all of the incident reports in the table
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            raw_data = JSON.parse(this.responseText);
            for (i = 0; i < raw_data.length; i++){
                incident_names[i] = raw_data[i].incid_name;
                incident_count[i] = raw_data[i].incident_count;
            }
            callback();
        }
    };
    xhttp.open("GET", "../PHP/retrieve_incident_data.php", true);
    xhttp.send();
}


function create_visualisation() {
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
// The type of chart we want to create
        type: 'bar',

// The data for our dataset
        data: {
            labels: incident_names,
            datasets: [{
                backgroundColor: ["#3e95cd", "#E5E500", "#c45850"],
                borderColor: 'rgb(255, 99, 132)',
                data: incident_count
            }]
        },

// Configuration options go here
        options: {
            title: {
                display: true,
                text: 'Sensor Incidents',
                fontSize: 24
            },
            legend: {
                display: false
            },
            scales: {
                yAxes: [{
                    ticks: {
                        stepSize: 1
                    }
                }]
            }
        }
    });
}
