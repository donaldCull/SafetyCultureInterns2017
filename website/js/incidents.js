// storage for the number of reports and its data
// this will be replaces when we get the data dynamically
var raw_data;
var reports = [];
var values = [];



window.onload = function start() {
    // runs the following functions when the pages load
    get_reports(function() {
        load_data();
    });


};

//document.getElementById("test_output").innerHTML = raw_data.length;


function load_data() {
    for (var i = 0; i < raw_data.length; i++){
        reports[i] = raw_data[i].pID;
    }


    var active = "active";
    for (i = 0; i < reports.length; i++){
        var link = "#";
        var id = "" + reports[i];
        var label = "" + reports[i];
        document.getElementById("reports_menu").innerHTML +=  "<a onclick='on_tab_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action "+ active +"\" id=\"" + id + "\">" + label + "</a>";
        active = "";
    }

// document.getElementById("test_output").innerHTML = reports;
}


function get_reports(callback) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200){
            raw_data = JSON.parse(this.responseText);
            callback();
        }
    };
    xhttp.open("GET", "../PHP/retrieve_Incidents.php", true);
    xhttp.send();
}

function report_menu_creation() {
    // populates the tab menu for the number of reports/incidents we have
    var active = "active";
    for (i = 0; i < reports.length; i++){
        var link = "#";
        var id = "" + reports[i];
        var label = "" + reports[i];
        document.getElementById("reports_menu").innerHTML +=  "<a onclick='on_tab_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action "+ active +"\" id=\"" + id + "\">" + label + "</a>";
        active = "";
    }
}

function table_population() {
    // populates the table with the data in values
    var report_table = document.getElementById("report_table");
    var values_count = 0;
    for(var i = 1; i < 8; i++){
        report_table.rows[i].cells[1].innerHTML = values[values_count];
        values_count++
    }
}

function on_tab_click(this_object) {
    // currently changes the list button item state when clicked
    // will add functionality to get and display the correct data
    var count = 1;
    for (var i = 0; i < reports.length; i++){
        var object_name = reports[i];
        var object = document.getElementById(object_name);
        $(object).removeClass("active");
        count++;

    }
    $(this_object).addClass("active");

}