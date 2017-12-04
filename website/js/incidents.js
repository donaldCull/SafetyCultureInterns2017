// storage for the IDs of reports and its data
var raw_data;
var sensors = [];
var unique_sensors = [];




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

    for (var x = 0; x < raw_data.length; x++){

        for (var y = 0; y < sensors.length; y++){

        }



    }




    for (var i = 0; i < raw_data.length; i++){
        var link = "#";
        var id = raw_data[i].incid_serial + " " + raw_data[i].pID;
        var label = "" + raw_data[i].incid_location + " - " + raw_data[i].incid_name;
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_tab_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action \" id=\"" + id + "\">" + label + "</a>";
    }

}