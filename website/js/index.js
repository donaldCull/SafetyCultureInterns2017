// storage for the number of reports and its data
// this will be replaces when we get the data dynamically
var reports = ["report 1","report 2","report 3","report 4","report 5","report 6","report 7","report 8",
    "report 9","report 10","report 11","report 12","report 13","report 14","report 15","report 16",
    "report 17","report 18","report 19","report 20","report 21","report 22","report 23","report 24","report 25"];

var values = [
    1.1,4.2,3.5,2.4,
    2.8,2.4,4.4,4.2,
    1.7,4.8,3.6,5.1,
    3.8,2.4,1.5,4.9,
    2.1,5.6,3.5,1.7,
    5.3,2.2,4.1,2.6,
    4.3,2.9,1.3,1.2
];

window.onload = function start() {
    // runs the following functions when the pages load
    report_menu_creation();
    table_population()
};

function report_menu_creation() {
    // populates the tab menu for the number of reports/incidents we have
    var active = "active";
    for (var i = 0; i < reports.length; i++){
        var link = "#";
        var id = "" + reports[i];
        var label = "" + reports[i];
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_tab_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action "+ active +"\" id=\"" + id + "\">" + label + "</a>";
        active = "";
    }
}

function table_population() {
    // populates the table with the data in values
    var report_table = document.getElementById("report_table");
    var values_count = 0;
    for (var x = 1; x < 8; x++){
    for(var i = 1; i < 5; i++){
        report_table.rows[x].cells[i].innerHTML = values[values_count];
        values_count++
        }
    }
}

function on_tab_click(this_object) {
    // currently changes the list button item state when clicked
    // will add functionality to get and display the correct data
    var count = 1;
    for (var i = 0; i < reports.length; i++){
        var object_name = "report " + count;
        var object = document.getElementById(object_name);
        $(object).removeClass("active");
        count++;

    }
    $(this_object).addClass("active");
}