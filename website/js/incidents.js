// storage for the IDs of reports and its data
var raw_data;
var report_id_list = [];


window.onload = function start() {
    // runs the following functions when the pages load
    get_raw_data(function () {
        create_menu_items();
        update_table(0);
    });
};


function create_menu_items() {
    // creates a list of IDs to user for the side menu
    for (var i = 0; i < raw_data.length; i++) {
        report_id_list[i] = raw_data[i].pID;
    }

    // creates and adds the menu items
    var active = "active";
    for (i = 0; i < report_id_list.length; i++) {
        var link = "#";
        var id = "" + report_id_list[i];
        var label = "#00" + report_id_list[i];
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_tab_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action " + active + "\" id=\"" + id + "\">" + label + "</a>";
        active = "";
    }
}


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


function on_tab_click(this_object) {
    // changes the list button item state when clicked
    var count = 0;
    for (var i = 0; i < report_id_list.length; i++) {
        var object_name = report_id_list[i];
        var object = document.getElementById(object_name);
        $(object).removeClass("active");
        count++;

    }
    $(this_object).addClass("active");


    // updates incident table based on selection
    var ob_id = this_object.id;
    ob_id -= 1;
    update_table(ob_id);
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