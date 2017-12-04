// storage for the number of reports and its data
var report_dates = [];
var report_data;
var report_id = 1;
var sensors = [];
var current_sensor = "Sensor_1";

window.onload = function start() {
    // runs the following functions when the pages load

    get_report(function () {
        getting_num_reports(function () {
            get_sensor_names();
            report_menu_creation();


        });
    });

};


function getting_num_reports(callback) {
    // gets the number of reports that there are in the database
    // in the form of the each report date
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            report_dates = JSON.parse(this.responseText);
            callback();
        }
    };
    xhttp.open("GET", "../PHP/retrieve_number_of_reports.php", true);
    xhttp.send();
}


function get_sensor_names() {
    // gets the names of each of the sensors in the data
    var count = 0;
    while (true) {

        if ((Object.keys(report_data)[count]) == undefined) {
            break;
        }
        else {
            sensors[count] = (Object.keys(report_data)[count]);
        }
        count++;
    }
}


function get_report(callback) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            var raw_data = JSON.parse(this.responseText);
            report_data = JSON.parse(raw_data[0].report_json);
            callback();
        }
    };
    xhttp.open("GET", "../PHP/retrieve_reports.php?q=" + report_id, true);
    xhttp.send();
}


function report_menu_creation() {
    // creates the side menu items based on the number of reports we have
    document.getElementById("reports_menu").innerHTML = "";
    var active = "";
    for (var i = 0; i < report_dates.length; i++) {
        var link = "#";
        var id = "" + (Object.keys(report_dates)[i]);
        var label = "" + report_dates[i].report_date;
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_tab_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action " + active + "\" id=\"" + id + "\">" + label + "</a>";
    }
}


function sensor_menu_creation() {
    document.getElementById("reports_menu").innerHTML = "";
    document.getElementById("reports_menu").innerHTML += "<a onclick='report_menu_creation()' class=\"list-group-item list-group-item-action\">Back</a>";
    var active = "active";
    for (var i = 0; i <sensors.length; i++){
        var link = "#";
        var id = "" + sensors[i];
        var label = "" + sensors[i];
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_sensor_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action " + active + "\" id=\"" + id + "\">" + label + "</a>";
        active = "";
    }
}


function on_sensor_click(this_object) {
    for (var i = 0; i < sensors.length; i++) {
        var object = document.getElementById(sensors[i]);
        $(object).removeClass("active");
    }
    $(this_object).addClass("active");


    current_sensor = this_object.id;

    update_table();


}


function on_tab_click(this_object) {
    // changes the list button item state when clicked

    sensor_menu_creation();

    // updates the reports table
    current_sensor = sensors[0];
    report_id = parseInt(this_object.id);
    report_id += 1;
    get_report(function () {
        update_table();
    });

}


function update_table() {
    // a stupid way to update the table, but it works so...
    var report_table = document.getElementById("report_table");
    var count = 0;
    for (var i = 1; i < 5; i++) {
        report_table.rows[1].cells[i].innerHTML = report_data[current_sensor]["Monday"][count];
        report_table.rows[2].cells[i].innerHTML = report_data[current_sensor]["Tuesday"][count];
        report_table.rows[3].cells[i].innerHTML = report_data[current_sensor]["Wednsday"][count];
        report_table.rows[4].cells[i].innerHTML = report_data[current_sensor]["Thursday"][count];
        report_table.rows[5].cells[i].innerHTML = report_data[current_sensor]["Friday"][count];
        report_table.rows[6].cells[i].innerHTML = report_data[current_sensor]["Saturday"][count];
        report_table.rows[7].cells[i].innerHTML = report_data[current_sensor]["Sunday"][count];
        count++;
    }
}