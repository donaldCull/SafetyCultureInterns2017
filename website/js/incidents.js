// storage for the IDs of reports and its data
var raw_data;
var sensors = [];
var sensor_info = [];
var current_sensor;




window.onload = function start() {
    // runs the following functions when the pages load
    get_raw_data(function () {
        sensors_menu();
    });
};



function get_raw_data(callback) {
    // connects to server to get all of the incident reports in the table
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            raw_data = JSON.parse(this.responseText);
            callback();
        }
    };
    xhttp.open("GET", "../PHP/retrieve_Incidents.php", true);
    xhttp.send();
}

function update_table(ob_id) {
    // a stupid way to update the table, but it works so...
    var report_table = document.getElementById("report_table");
    report_table.rows[0].cells[1].innerHTML = raw_data[ob_id].pID;
    report_table.rows[1].cells[1].innerHTML = raw_data[ob_id].incid_serial;
    report_table.rows[2].cells[1].innerHTML = raw_data[ob_id].incid_location;
    report_table.rows[3].cells[1].innerHTML = raw_data[ob_id].incid_name;
    report_table.rows[4].cells[1].innerHTML = raw_data[ob_id].incid_date_start;
    report_table.rows[5].cells[1].innerHTML = raw_data[ob_id].incid_time_start;
    report_table.rows[6].cells[1].innerHTML = raw_data[ob_id].incid_temp;
    report_table.rows[7].cells[1].innerHTML = raw_data[ob_id].incid_date_stop;
    report_table.rows[8].cells[1].innerHTML = raw_data[ob_id].incid_time_stop;

}

function sensors_menu() {
    // finds unique sensors
    var add = true;
    sensors.push(raw_data[0].incid_serial);
    for (var g = 0; g < raw_data.length; g++){
        add = true;

        for (var x = 0; x < sensors.length; x++){
            if (sensors[x] === raw_data[g].incid_serial){
                add = false;
            }
        }
        if (add){
            sensors.push(raw_data[g].incid_serial)
        }
    }

    // get sensor info
    for (var w = 0; w < sensors.length; w++){
        for (g = 0; g < raw_data.length; g++){
            if(sensors[w] === raw_data[g].incid_serial){
                sensor_info[sensors[w]] = [raw_data[g].incid_location, raw_data[g].incid_name]
            }
        }

    }

    // create menu items
    for (var i = 0; i < sensors.length; i++){
        var link = "#";
        var id = "" + sensors[i];
        var label = "" + sensor_info[sensors[i]][0] + " - " + sensor_info[sensors[i]][1];
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_sensor_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action \" id=\"" + id + "\">" + label + "</a>";
    }

}

function on_sensor_click(this_object) {
    document.getElementById("reports_menu").innerHTML = "";
    current_sensor = this_object.id;

    for (var i = 0; i < raw_data.length; i++){
        if (raw_data[i].incid_serial === current_sensor){
            var link = "#";
            var id = "" + raw_data[i].pID;
            var label = "" + raw_data[i].pID;
            document.getElementById("reports_menu").innerHTML += "<a onclick='on_report_click(this_object)' href=\"" + link + "\" class=\"list-group-item list-group-item-action \" id=\"" + id + "\">" + label + "</a>"
        }
    }
}

function on_report_click(this_object) {

}