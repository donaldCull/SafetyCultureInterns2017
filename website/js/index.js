// storage for the number of reports and its data
// this will be replaces when we get the data dynamically
var report_dates = [];
var report_data;
var report_id = 1;
var sensors = [];
var current_sensor = "Sensor_1";

window.onload = function start() {
    // runs the following functions when the pages load

    getting_num_reports(function() {
        get_sensor_names();
        report_menu_creation()
    });

    retrieveReport(function() {
        update_table();
    })


};


function get_sensor_names() {

    var count = 0;
    while (true){

        if((Object.keys(report_data)[count]) == undefined){
            break;
        }
        else {
            sensors[count] = (Object.keys(report_data)[count]);
        }
        count++;
    }

    for (i = 0; i < sensors.length; i++){
        var id = sensors[i];
        var label = sensors[i];

        document.getElementById("sensor_list_dropdown").innerHTML += "<a id='"+ id +"' onclick='on_sensor_click(this)' class='dropdown-item' href='#'>"+ label + "</a>";
    }
    current_sensor = sensors[0];
}


function getting_num_reports(callback) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200){
            report_dates = JSON.parse(this.responseText);
            callback();
        }
    };
    xhttp.open("GET", "../PHP/retrieve_number_of_reports.php", true);
    xhttp.send();



}


function report_menu_creation() {
    // populates the tab menu for the number of reports/incidents we have
    var active = "active";
    for (var i = 0; i < report_dates.length; i++){
        var link = "#";
        var id = "" + (Object.keys(report_dates)[i]);
        var label = "" + report_dates[i].report_date;
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_tab_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action "+ active +"\" id=\"" + id + "\">" + label + "</a>";
        active = "";
    }
}


function retrieveReport(callback) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200){
            var raw_data = JSON.parse(this.responseText);
            report_data = JSON.parse(raw_data[0].report_json);
            callback();
        }
    };
    xhttp.open("GET", "../PHP/retrieve_reports.php?q="+report_id, true);
    xhttp.send();
}


function on_tab_click(this_object) {
    // currently changes the list button item state when clicked
    // will add functionality to get and display the correct data


    // The count is the primary key of the report in the database
    for (var i = 0; i < report_dates.length; i++){
        var object = document.getElementById(i);
        $(object).removeClass("active");

    }
    $(this_object).addClass("active");


    report_id = parseInt(this_object.id);
    report_id += 1;



    retrieveReport(function() {
        update_table();
    })

}


function update_table() {
    var report_table = document.getElementById("report_table");
    var count = 0;
    for (var i = 1; i < 5; i++){
        report_table.rows[1].cells[i].innerHTML = report_data[current_sensor]["Monday"][count];
        report_table.rows[2].cells[i].innerHTML = report_data["Sensor_1"]["Tuesday"][count];
        report_table.rows[3].cells[i].innerHTML = report_data["Sensor_1"]["Wednsday"][count];
        report_table.rows[4].cells[i].innerHTML = report_data["Sensor_1"]["Thursday"][count];
        report_table.rows[5].cells[i].innerHTML = report_data["Sensor_1"]["Friday"][count];
        report_table.rows[6].cells[i].innerHTML = report_data["Sensor_1"]["Saturday"][count];
        report_table.rows[7].cells[i].innerHTML = report_data["Sensor_1"]["Sunday"][count];
        count++;
    }

}

function on_sensor_click(object) {
    current_sensor = object.id;
    update_table();
}