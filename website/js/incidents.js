// storage for the number of reports and its data
// this will be replaces when we get the data dynamically
var raw_data;
var reports = [];
var values = [];


window.onload = function start() {
    // runs the following functions when the pages load
    get_reports(function () {
        load_data();
        update_table(0);
    });
};


function load_data() {
    for (var i = 0; i < raw_data.length; i++) {
        reports[i] = raw_data[i].pID;
    }

    var active = "active";
    for (i = 0; i < reports.length; i++) {
        var link = "#";
        var id = "" + reports[i];
        var label = "#00" + reports[i];
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_tab_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action " + active + "\" id=\"" + id + "\">" + label + "</a>";
        active = "";
    }


// document.getElementById("test_output").innerHTML = reports;
}

function get_reports(callback) {
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

function on_tab_click(this_object) {
    // currently changes the list button item state when clicked
    // will add functionality to get and display the correct data
    var count = 0;
    for (var i = 0; i < reports.length; i++) {
        var object_name = reports[i];
        var object = document.getElementById(object_name);
        $(object).removeClass("active");
        count++;

    }
    $(this_object).addClass("active");


    // update table based on selection

    var ob_id = this_object.id;
    ob_id -= 1;

    update_table(ob_id);


}

function update_table(ob_id) {
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