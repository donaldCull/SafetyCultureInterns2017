// storage for the number of reports and its data
var report_dates = [];
var report_data;
var report_id = 1;
var sensors = [];
var current_sensor;
var days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
var raw_data;

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
        if ((Object.keys(report_data["report_json"])[count]) == undefined) {
            break;
        }
        else {
            sensors[count] = (Object.keys(report_data["report_json"])[count]);
        }
        count++;
    }
    sensors.pop();
    sensors.pop();

}


function get_report(callback) {
    // gets the report needed with the report id
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            raw_data = JSON.parse(this.responseText);
            report_data = raw_data[0];
            report_data["report_json"] =  JSON.parse(report_data["report_json"]);

            callback();
        }
    };
    xhttp.open("GET", "../PHP/retrieve_reports.php?q=" + report_id, true);
    xhttp.send();
}


function report_menu_creation() {
    // creates the side menu items based on the number of reports we have
    document.getElementById("reports_menu").innerHTML = "";
    document.getElementById("data_table").innerHTML = "<p id=\"data_table_no_data_selected\">No data selected<br>Please select from menu</p>";


    var active = "";
    for (var i = 0; i < report_dates.length; i++) {
        var link = "#";
        var id = "" + (Object.keys(report_dates)[i]);
        var label = "" + report_dates[i].report_date;
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_report_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action " + active + "\" id=\"" + id + "\">" + label + "</a>";
    }
}


function sensor_menu_creation() {
    // creates the menu items for each of the sensors we have
    document.getElementById("reports_menu").innerHTML = "";
    document.getElementById("reports_menu").innerHTML += "<a onclick='report_menu_creation()' class=\"list-group-item list-group-item-action\">Back</a>";
    var active = "";
    for (var i = 0; i <sensors.length; i++){
        var link = "#";
        var id = "" + sensors[i];
        var label = "" + sensors[i];
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_sensor_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action " + active + "\" id=\"" + id + "\">" + label + "</a>";
        active = "";
    }
}


function update_table() {
    document.getElementById("data_table").innerHTML = "";

    // create table
    var table = document.createElement("TABLE");
    var thead = document.createElement("THEAD");
    var tbody = document.createElement("TBODY");
    table.setAttribute("id", "report_table");
    thead.setAttribute("id", "report_table_head");
    tbody.setAttribute("id", "report_table_tbody");
    document.getElementById("data_table").appendChild(table);
    document.getElementById("report_table").appendChild(thead);
    document.getElementById("report_table").appendChild(tbody);


    for (var x = 0; x < days.length; x++){
        add_row(days[x])
    }


    document.getElementById("data_table").innerHTML += "<div id=\"print_download_btns\"><button onclick=\"window.print();return false;\" type=\"button\" class=\"btn btn-primary\">Print</button></div>";

    $(report_table).addClass("table table-hover table-bordered");
    $(report_table_head).addClass("thead-light");




}

function add_row(day) {
    var tr = "tr_" + day;

    var tr_mon = document.createElement("TR");
    tr_mon.setAttribute("id", tr);
    document.getElementById("report_table_tbody").appendChild(tr_mon);

    var th_mon = document.createElement("TH");
    x = document.createTextNode(day);
    th_mon.appendChild(x);
    document.getElementById(tr).appendChild(th_mon);


    if (report_data.report_json[current_sensor][day].length >= 2){
        var cell_2 = document.createElement("TD");
        x = document.createTextNode("" + report_data.report_json[current_sensor][day][0]);
        cell_2.appendChild(x);
        document.getElementById(tr).appendChild(cell_2);

        var cell_3 = document.createElement("TD");
        x = document.createTextNode("" + report_data.report_json[current_sensor][day][1]);
        cell_3.appendChild(x);
        document.getElementById(tr).appendChild(cell_3);
    }

    if (report_data.report_json[current_sensor][day].length >= 3){
        var cell_4 = document.createElement("TD");
        x = document.createTextNode("" + report_data.report_json[current_sensor][day][2]);
        cell_4.appendChild(x);
        document.getElementById(tr).appendChild(cell_4);
    }

    if (report_data.report_json[current_sensor][day].length >= 4){
        var cell_5 = document.createElement("TD");
        x = document.createTextNode("" + report_data.report_json[current_sensor][day][3]);
        cell_5.appendChild(x);
        document.getElementById(tr).appendChild(cell_5);
    }

    if (report_data.report_json[current_sensor][day].length >= 5){
        var cell_6 = document.createElement("TD");
        x = document.createTextNode("" + report_data.report_json[current_sensor][day][4]);
        cell_6.appendChild(x);
        document.getElementById(tr).appendChild(cell_6);
    }

    if (report_data.report_json[current_sensor][day].length >= 6){
        var cell_7 = document.createElement("TD");
        x = document.createTextNode("" + report_data.report_json[current_sensor][day][5]);
        cell_7.appendChild(x);
        document.getElementById(tr).appendChild(cell_7);
    }

}

function on_sensor_click(this_object) {
    // function runs when the sensors button is clicked
    // changes the active state of the other items and self
    // updates the table getting the correct report
    for (var i = 0; i < sensors.length; i++) {
        var object = document.getElementById(sensors[i]);
        $(object).removeClass("active");
    }
    $(this_object).addClass("active");


    current_sensor = this_object.id;

    update_table();


}


function on_report_click(this_object) {
    // changes the list button item state when clicked

    sensor_menu_creation();

    // updates the reports table
    current_sensor = sensors[0];
    report_id = parseInt(this_object.id);
    report_id += 1;
    get_report(function () {

    });

}