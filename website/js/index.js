// storage for the number of reports and its data
var report_dates = [];
var report_data;
var report_id = 1;
var sensors = [];
var current_sensor;


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
    // gets the report needed with the report id
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

    // table headings
    var tr = document.createElement("TR");
    tr.setAttribute("id", "report_table_head_tr");
    document.getElementById("report_table_head").appendChild(tr);

    var theader1 = document.createElement("TH");
    var x = document.createTextNode("Date");
    theader1.appendChild(x);
    document.getElementById("report_table_head_tr").appendChild(theader1);

    var theader2 = document.createElement("TH");
    x = document.createTextNode("8am");
    theader2.appendChild(x);
    document.getElementById("report_table_head_tr").appendChild(theader2);

    var theader3 = document.createElement("TH");
    x = document.createTextNode("10am");
    theader3.appendChild(x);
    document.getElementById("report_table_head_tr").appendChild(theader3);

    var theader4 = document.createElement("TH");
    x = document.createTextNode("2pm");
    theader4.appendChild(x);
    document.getElementById("report_table_head_tr").appendChild(theader4);

    var theader5 = document.createElement("TH");
    x = document.createTextNode("10pm");
    theader5.appendChild(x);
    document.getElementById("report_table_head_tr").appendChild(theader5);


    // row monday
    var tr_mon = document.createElement("TR");
    tr_mon.setAttribute("id", "tr_mon");
    document.getElementById("report_table_tbody").appendChild(tr_mon);

    var th_mon = document.createElement("TH");
    x = document.createTextNode("Monday:");
    th_mon.appendChild(x);
    document.getElementById("tr_mon").appendChild(th_mon);

    var td1_mon = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Monday"][0]);
    td1_mon.appendChild(x);
    document.getElementById("tr_mon").appendChild(td1_mon);

    var td2_mon = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Monday"][1]);
    td2_mon.appendChild(x);
    document.getElementById("tr_mon").appendChild(td2_mon);

    var td3_mon = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Monday"][2]);
    td3_mon.appendChild(x);
    document.getElementById("tr_mon").appendChild(td3_mon);

    var td4_mon = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Monday"][3]);
    td4_mon.appendChild(x);
    document.getElementById("tr_mon").appendChild(td4_mon);


    // row tuesday
    var tr_tue = document.createElement("TR");
    tr_tue.setAttribute("id", "tr_tue");
    document.getElementById("report_table_tbody").appendChild(tr_tue);

    var th_tue = document.createElement("TH");
    x = document.createTextNode("Tuesday:");
    th_tue.appendChild(x);
    document.getElementById("tr_tue").appendChild(th_tue);

    var td1_tue = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Tuesday"][0]);
    td1_tue.appendChild(x);
    document.getElementById("tr_tue").appendChild(td1_tue);

    var td2_tue = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Tuesday"][1]);
    td2_tue.appendChild(x);
    document.getElementById("tr_tue").appendChild(td2_tue);

    var td3_tue = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Tuesday"][2]);
    td3_tue.appendChild(x);
    document.getElementById("tr_tue").appendChild(td3_tue);

    var td4_tue = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Tuesday"][3]);
    td4_tue.appendChild(x);
    document.getElementById("tr_tue").appendChild(td4_tue);


    //row wednsday
    var tr_wed = document.createElement("TR");
    tr_wed.setAttribute("id", "tr_wed");
    document.getElementById("report_table_tbody").appendChild(tr_wed);

    var th_wed = document.createElement("TH");
    x = document.createTextNode("Wednsday:");
    th_wed.appendChild(x);
    document.getElementById("tr_wed").appendChild(th_wed);

    var td1_wed = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Wednsday"][0]);
    td1_wed.appendChild(x);
    document.getElementById("tr_wed").appendChild(td1_wed);

    var td2_wed = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Wednsday"][1]);
    td2_wed.appendChild(x);
    document.getElementById("tr_wed").appendChild(td2_wed);

    var td3_wed = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Wednsday"][2]);
    td3_wed.appendChild(x);
    document.getElementById("tr_wed").appendChild(td3_wed);

    var td4_wed = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Wednsday"][3]);
    td4_wed.appendChild(x);
    document.getElementById("tr_wed").appendChild(td4_wed);


    //row thursday
    var tr_thu = document.createElement("TR");
    tr_thu.setAttribute("id", "tr_thu");
    document.getElementById("report_table_tbody").appendChild(tr_thu);

    var th_thu = document.createElement("TH");
    x = document.createTextNode("Thursday:");
    th_thu.appendChild(x);
    document.getElementById("tr_thu").appendChild(th_thu);

    var td1_thu = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Thursday"][0]);
    td1_thu.appendChild(x);
    document.getElementById("tr_thu").appendChild(td1_thu);

    var td2_thu = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Thursday"][1]);
    td2_thu.appendChild(x);
    document.getElementById("tr_thu").appendChild(td2_thu);

    var td3_thu = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Thursday"][2]);
    td3_thu.appendChild(x);
    document.getElementById("tr_thu").appendChild(td3_thu);

    var td4_thu = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Thursday"][3]);
    td4_thu.appendChild(x);
    document.getElementById("tr_thu").appendChild(td4_thu);

    $(report_table).addClass("table table-hover table-bordered");
    $(report_table_head).addClass("thead-light");



    //row friday
    var tr_fri = document.createElement("TR");
    tr_fri.setAttribute("id", "tr_fri");
    document.getElementById("report_table_tbody").appendChild(tr_fri);

    var th_fri = document.createElement("TH");
    x = document.createTextNode("Friday:");
    th_fri.appendChild(x);
    document.getElementById("tr_fri").appendChild(th_fri);

    var td1_fri = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Friday"][0]);
    td1_fri.appendChild(x);
    document.getElementById("tr_fri").appendChild(td1_fri);

    var td2_fri = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Friday"][1]);
    td2_fri.appendChild(x);
    document.getElementById("tr_fri").appendChild(td2_fri);

    var td3_fri = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Friday"][2]);
    td3_fri.appendChild(x);
    document.getElementById("tr_fri").appendChild(td3_fri);

    var td4_fri = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Friday"][3]);
    td4_fri.appendChild(x);
    document.getElementById("tr_fri").appendChild(td4_fri);

    $(report_table).addClass("table table-hover table-bordered");
    $(report_table_head).addClass("thead-light");



    //row saturday
    var tr_sat = document.createElement("TR");
    tr_sat.setAttribute("id", "tr_sat");
    document.getElementById("report_table_tbody").appendChild(tr_sat);

    var th_sat = document.createElement("TH");
    x = document.createTextNode("Saturday:");
    th_sat.appendChild(x);
    document.getElementById("tr_sat").appendChild(th_sat);

    var td1_sat = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Saturday"][0]);
    td1_sat.appendChild(x);
    document.getElementById("tr_sat").appendChild(td1_sat);

    var td2_sat = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Saturday"][1]);
    td2_sat.appendChild(x);
    document.getElementById("tr_sat").appendChild(td2_sat);

    var td3_sat = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Saturday"][2]);
    td3_sat.appendChild(x);
    document.getElementById("tr_sat").appendChild(td3_sat);

    var td4_sat = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Saturday"][3]);
    td4_sat.appendChild(x);
    document.getElementById("tr_sat").appendChild(td4_sat);

    $(report_table).addClass("table table-hover table-bordered");
    $(report_table_head).addClass("thead-light");


    //row sun
    var tr_sun = document.createElement("TR");
    tr_sun.setAttribute("id", "tr_sun");
    document.getElementById("report_table_tbody").appendChild(tr_sun);

    var th_sun = document.createElement("TH");
    x = document.createTextNode("Sunday:");
    th_sun.appendChild(x);
    document.getElementById("tr_sun").appendChild(th_sun);

    var td1_sun = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Sunday"][0]);
    td1_sun.appendChild(x);
    document.getElementById("tr_sun").appendChild(td1_sun);

    var td2_sun = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Sunday"][1]);
    td2_sun.appendChild(x);
    document.getElementById("tr_sun").appendChild(td2_sun);

    var td3_sun = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Sunday"][2]);
    td3_sun.appendChild(x);
    document.getElementById("tr_sun").appendChild(td3_sun);

    var td4_sun = document.createElement("TD");
    x = document.createTextNode("" + report_data[current_sensor]["Sunday"][3]);
    td4_sun.appendChild(x);
    document.getElementById("tr_sun").appendChild(td4_sun);

    $(report_table).addClass("table table-hover table-bordered");
    $(report_table_head).addClass("thead-light");




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