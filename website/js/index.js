// storage for the number of reports and its data
// this will be replaces when we get the data dynamically


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

function retrieveReport() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200){
            raw_data = JSON.parse(this.responseText);
            report_data = JSON.parse(raw_data[0].report_json);
            //document.getElementById("test_output").innerHTML = raw_data[0].report_json;
            callback();
        }
    };
    xhttp.open("GET", "../PHP/retrieve_reports.php?q="+1, true);
    xhttp.send();
}



function on_tab_click(this_object) {
    // currently changes the list button item state when clicked
    // will add functionality to get and display the correct data

    var count = 1;
    // The count is the primary key of the report in the database
    var id = this_object.id;
    retrieveReport(id);
    for (var i = 0; i < reports.length; i++){
        var object_name = "report " + count;
        var object = document.getElementById(object_name);
        $(object).removeClass("active");
        count++;

    }
    $(this_object).addClass("active");
}