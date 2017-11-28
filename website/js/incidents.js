// storage for the number of reports and its data
// this will be replaces when we get the data dynamically
var reports = ["Incident 1","Incident 2","Incident 3","Incident 4","Incident 5","Incident 6"];
var values = ["4852F6TH01","Kitchen","Drinks Fridge","25/4/17 12:35:15","7.8","25/4/17 12:52:45","4.5"];

window.onload = function start() {
    // runs the following functions when the pages load
    report_menu_creation();
    table_population();

};

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
        var object_name = "Incident " + count;
        var object = document.getElementById(object_name);
        $(object).removeClass("active");
        count++;

    }
    $(this_object).addClass("active");
}