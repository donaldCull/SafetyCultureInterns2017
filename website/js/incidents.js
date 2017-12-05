// storage for the IDs of reports and its data
var raw_data;
var sensors = [];
var sensor_info = [];
var current_sensor;
var current_report;


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
    create_menu();
}


function create_menu() {
    // creates the initial menu for each individual sensor
    document.getElementById("reports_menu").innerHTML = "";
    document.getElementById("data_table").innerHTML = "<p id=\"data_table_no_data_selected\">No data selected<br>Please select from menu</p>";

    // create menu items
    for (var i = 0; i < sensors.length; i++){
        var link = "#";
        var id = "" + sensors[i];
        var label = "" + sensor_info[sensors[i]][0] + " - " + sensor_info[sensors[i]][1];
        document.getElementById("reports_menu").innerHTML += "<a onclick='on_sensor_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action \" id=\"" + id + "\">" + label + "</a>";
    }

}


function update_table() {
    document.getElementById("data_table").innerHTML = "";
    console.log("HELLO WORLD");


    // creates table
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
    var thead = document.createElement("THEAD");
    thead.setAttribute("id", "report_table_head");
    document.getElementById("report_table_tbody").appendChild(thead);


    var tr = document.createElement("TR");
    tr.setAttribute("id", "report_table_head_tr");
    document.getElementById("report_table_head").appendChild(tr);

    var theader1 = document.createElement("TH");
    var x = document.createTextNode("Incident: ");
    theader1.appendChild(x);
    document.getElementById("report_table_head_tr").appendChild(theader1);

    var theader2 = document.createElement("TH");
    x = document.createTextNode("#0000" + raw_data[current_report].pID);
    theader2.appendChild(x);
    document.getElementById("report_table_head_tr").appendChild(theader2);


    // row 1
    var tr1 = document.createElement("TR");
    tr1.setAttribute("id", "tr1");
    document.getElementById("report_table_tbody").appendChild(tr1);

    var th1 = document.createElement("TH");
    x = document.createTextNode("Serial:");
    th1.appendChild(x);
    document.getElementById("tr1").appendChild(th1);

    var td1 = document.createElement("TD");
    x = document.createTextNode("" + raw_data[current_report].incid_serial);
    td1.appendChild(x);
    document.getElementById("tr1").appendChild(td1);

    // row 2
    var tr2 = document.createElement("TR");
    tr2.setAttribute("id", "tr2");
    document.getElementById("report_table_tbody").appendChild(tr2);

    var th2 = document.createElement("TH");
    x = document.createTextNode("Location:");
    th2.appendChild(x);
    document.getElementById("tr2").appendChild(th2);

    var td2 = document.createElement("TD");
    x = document.createTextNode("" + raw_data[current_report].incid_location);
    td2.appendChild(x);
    document.getElementById("tr2").appendChild(td2);


    // row 3
    var tr3 = document.createElement("TR");
    tr3.setAttribute("id", "tr3");
    document.getElementById("report_table_tbody").appendChild(tr3);

    var th3 = document.createElement("TH");
    x = document.createTextNode("Device:");
    th3.appendChild(x);
    document.getElementById("tr3").appendChild(th3);

    var td3 = document.createElement("TD");
    x = document.createTextNode("" + raw_data[current_report].incid_name);
    td3.appendChild(x);
    document.getElementById("tr3").appendChild(td3);

    //row 4
    var tr4 = document.createElement("TR");
    tr4.setAttribute("id", "tr4");
    document.getElementById("report_table_tbody").appendChild(tr4);

    var th4 = document.createElement("TH");
    x = document.createTextNode("Date/Time incident:");
    th4.appendChild(x);
    document.getElementById("tr4").appendChild(th4);

    var td4 = document.createElement("TD");
    x = document.createTextNode("" + raw_data[current_report].incid_date_start + " / " + raw_data[current_report].incid_time_start);
    td4.appendChild(x);
    document.getElementById("tr4").appendChild(td4);


    // row 5
    var tr5 = document.createElement("TR");
    tr5.setAttribute("id", "tr5");
    document.getElementById("report_table_tbody").appendChild(tr5);

    var th5 = document.createElement("TH");
    x = document.createTextNode("Temperature:");
    th5.appendChild(x);
    document.getElementById("tr5").appendChild(th5);

    var td5 = document.createElement("TD");
    x = document.createTextNode("" + raw_data[current_report].incid_temp);
    td5.appendChild(x);
    document.getElementById("tr5").appendChild(td5);

    // row 6
    var tr6 = document.createElement("TR");
    tr6.setAttribute("id", "tr6");
    document.getElementById("report_table_tbody").appendChild(tr6);

    var th6 = document.createElement("TH");
    x = document.createTextNode("Date/Time resolved:");
    th6.appendChild(x);
    document.getElementById("tr6").appendChild(th6);

    var td6 = document.createElement("TD");
    x = document.createTextNode("" + raw_data[current_report].incid_date_stop + " / " + raw_data[current_report].incid_time_stop);
    td6.appendChild(x);
    document.getElementById("tr6").appendChild(td6);



    $(report_table).addClass("table table-hover table-bordered");
    $(report_table_head).addClass("thead-light");

}


function on_sensor_click(this_object) {
    // function runs when the sensors button is clicked
    // changes the active state of the other items and self
    // updates the table getting the correct report
    document.getElementById("reports_menu").innerHTML = "";
    current_sensor = this_object.id;

    document.getElementById("reports_menu").innerHTML += "<a onclick='create_menu()'  class=\"list-group-item list-group-item-action \">Back</a>"
    for (var i = 0; i < raw_data.length; i++){
        if (raw_data[i].incid_serial === current_sensor){
            var link = "#";
            var id = "" + raw_data[i].pID;
            var label = "" + raw_data[i].pID;
            document.getElementById("reports_menu").innerHTML += "<a onclick='on_report_click(this)' href=\"" + link + "\" class=\"list-group-item list-group-item-action \" id=\"" + id + "\">" + label + "</a>"
        }
    }
}


function on_report_click(obj) {
    // changes the list button item state when clicked
    current_report = obj.id;
    current_report -= 1;
    for (var i = 0; i < raw_data.length+1; i++) {
        var object = document.getElementById("" + i);
        $(object).removeClass("active");
    }
    $(obj).addClass("active");
    update_table();
}