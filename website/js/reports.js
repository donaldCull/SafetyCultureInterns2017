// storage for the number of reports and its data
var report_dates = [];
var search_dates = [];
var report_data;
var report_id = 1;
var sensors = [];
var sensor_names;
var current_sensor;
var days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
var raw_data;
var dates_count = 0;

window.onload = function start() {
    // runs the following functions when the pages load

    get_sensors(function (){
            getting_num_reports(function () {
                get_sensor_names();
                search_dates = report_dates;
                sensor_menu_creation()

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
    for (var i = 0; i < sensor_names.length; i++) {
        if (sensor_names[count]["sens_serial"] === undefined){
            break;
        }
        else {
            sensors[count] = sensor_names[count]["sens_serial"];
        }
        count++;
    }

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


function get_sensors(callback) {
    // get each sensor from the devicelist table
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            sensor_names = JSON.parse(this.responseText);
            callback();
        }
    };
    xhttp.open("GET", "../PHP/retrieve_sensors.php", true);
    xhttp.send();

}


function report_menu_creation() {
    // creates the side menu items based on the number of reports we have
    document.getElementById("reports_menu").innerHTML = "";
    document.getElementById("reports_menu").innerHTML += "<a onclick='sensor_menu_creation()' class=\"list-group-item list-group-item-action bg-transparent border-light small text-light \">Back</a>";



    var active = "";
    for (var i = 0; i < search_dates.length; i++) {
        var link = "#";
        var id = "" + (Object.keys(search_dates)[i]);
        var label = "" + search_dates[i].report_date + " - #" + i;
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_report_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action bg-transparent border-light text-light small " + active + "\" id=\"" + id + "\">" + label + "</a>";
    }
}


function sensor_menu_creation() {
    // creates the menu items for each of the sensors we have
    document.getElementById("reports_menu").innerHTML = "";
    document.getElementById("data_table").innerHTML = "<p id=\"data_table_no_data_selected\">No data selected<br>Please select from menu</p>";

    var active = "";
    for (var i = 0; i <sensors.length; i++){
        var link = "#";
        var id = "" + sensors[i];
        var label = "" + sensor_names[i]["sens_location"] + " - " + sensor_names[i]["sens_name"];
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_sensor_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action bg-transparent border-light text-light small" + active + "\" id=\"" + id + "\">" + label + "</a>";
        active = "";
    }
}


function update_table() {
    dates_count = 0;
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
    var x = document.createTextNode("");
    theader1.appendChild(x);
    document.getElementById("report_table_head_tr").appendChild(theader1);



    if (report_data.report_json.Times.length >= 2){
        var theader2 = document.createElement("TH");
        x = document.createTextNode(convert_time(report_data.report_json.Times[0]));
        theader2.appendChild(x);
        document.getElementById("report_table_head_tr").appendChild(theader2);

        var theader3 = document.createElement("TH");
        x = document.createTextNode(convert_time(report_data.report_json.Times[1]));
        theader3.appendChild(x);
        document.getElementById("report_table_head_tr").appendChild(theader3);
    }

    if (report_data.report_json.Times.length >= 3){
        var theader4 = document.createElement("TH");
        x = document.createTextNode(convert_time(report_data.report_json.Times[2]));
        theader4.appendChild(x);
        document.getElementById("report_table_head_tr").appendChild(theader4);
    }

    if (report_data.report_json.Times.length >= 4){
        var theader5 = document.createElement("TH");
        x = document.createTextNode(convert_time(report_data.report_json.Times[3]));
        theader5.appendChild(x);
        document.getElementById("report_table_head_tr").appendChild(theader5);
    }

    if (report_data.report_json.Times.length >= 5){

    }

    if (report_data.report_json.Times.length >= 6){

    }






    for (var o = 0; o < days.length; o++){
        add_row(days[o])
    }


    // document.getElementById("data_table").innerHTML += "<div id=\"print_download_btns\"><button " +
    //     "onclick=\"window.print();return false;\" type=\"button\" class=\"btn btn-primary\">Print</button></div>";

    $(report_table).addClass("table table-bordered");
    $(report_table_head).addClass("thead-light");




}


function convert_time(time_24h) {
    var return_time;

    if (time_24h > 0 && time_24h < 12){
        return_time = time_24h + ":00am"
    }
    else if (time_24h > 12){
        time_24h -= 12;
        return_time = time_24h + ":00pm"
    }
    else if (time_24h === 0){
        return_time = "12:00am"
    }
    else if (time_24h === 12){
        return_time = "12:00pm"
    }

    return return_time;
}


function add_row(day) {
    var tr = "tr_" + day;

    var tr_mon = document.createElement("TR");
    tr_mon.setAttribute("id", tr);
    document.getElementById("report_table_tbody").appendChild(tr_mon);

    var th_mon = document.createElement("TH");
    x = document.createTextNode(day);
    y = document.createElement("BR");
    z = document.createTextNode(report_data.report_json["Dates"][dates_count]);
    th_mon.appendChild(x);
    th_mon.appendChild(y);
    th_mon.appendChild(z);
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

    dates_count++;

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

    report_menu_creation();



}


function on_report_click(this_object) {
    // changes the list button item state when clicked



    // updates the reports table
    report_id = parseInt(this_object.id);
    report_id += 1;
    get_report(function () {
        update_table();
    });


}


function on_search_dates_click() {
    var search_par = document.getElementById("date_search_param").value;
    var search_month = document.getElementById("date_search_month").value;
    var search_year = document.getElementById("date_search_year").value;

    if (search_month === "Jan"){search_month = "1"}
    else if (search_month === "Feb"){search_month = "2"}
    else if (search_month === "Mar"){search_month = "3"}
    else if (search_month === "Apr"){search_month = "4"}
    else if (search_month === "May"){search_month = "5"}
    else if (search_month === "Jun"){search_month = "6"}
    else if (search_month === "Jul"){search_month = "7"}
    else if (search_month === "Aug"){search_month = "8"}
    else if (search_month === "Sep"){search_month = "9"}
    else if (search_month === "Oct"){search_month = "10"}
    else if (search_month === "Nov"){search_month = "11"}
    else if (search_month === "Dec"){search_month = "12"}

    var new_dates = [];

    for (var i = 0; i < report_dates.length; i++) {
        var report_year;
        var report_month;
        report_year = report_dates[i]["report_date"].charAt(0);
        report_year += report_dates[i]["report_date"].charAt(1);
        report_year += report_dates[i]["report_date"].charAt(2);
        report_year += report_dates[i]["report_date"].charAt(3);
        report_month = report_dates[i]["report_date"].charAt(5);
        report_month += report_dates[i]["report_date"].charAt(6);


        if (search_par === "Exactly"){
            if(search_year === "Any"){
                if (report_month === search_month) {
                    new_dates.push(report_dates[i]);
                }
            }
            else if (search_month === "Any"){
                if (report_year === search_year) {
                    new_dates.push(report_dates[i]);
                }
            }
            else {
                if (report_year === search_year && report_month === search_month) {
                    new_dates.push(report_dates[i]);
                }
            }
        }
        else if (search_par === "Before"){
            if(search_year === "Any"){
                if (parseInt(report_month) >= parseInt(search_month)) {
                    new_dates.push(report_dates[i]);
                }
            }
            else if (search_month === "Any"){
                if (parseInt(report_year) >= parseInt(search_year)) {
                    new_dates.push(report_dates[i]);
                }
            }
            else {
                if (parseInt(report_year) >= parseInt(search_year)) {
                    new_dates.push(report_dates[i]);
                }
            }
        }
        else if (search_par === "After"){
            if(search_year === "Any"){
                if (parseInt(report_month) <= parseInt(search_month)) {
                    new_dates.push(report_dates[i]);
                }
            }
            else if (search_month === "Any"){
                if (parseInt(report_year) <= parseInt(search_year)) {
                    new_dates.push(report_dates[i]);
                }
            }
            else {
                if (parseInt(report_year) <= parseInt(search_year)) {
                    new_dates.push(report_dates[i]);
                }
            }
        }



    }

    if (search_month === "Any" && search_year === "Any"){
        search_dates = [];
        search_dates = report_dates;
        report_menu_creation();
    }
    else {
        search_dates = [];
        search_dates = new_dates;
        report_menu_creation();
    }


}


function on_reset_serch_dates_click() {
    search_dates = [];
    search_dates = report_dates;
    report_menu_creation();
}