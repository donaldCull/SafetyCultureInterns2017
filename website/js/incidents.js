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
    document.getElementById("data_table").innerHTML = "<p>Select a item from <<<</p>";

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
    var table = document.createElement("TABLE");
    var thead = document.createElement("THEAD");
    var tr = document.createElement("TR");
    var td = document.createElement("TD");



    table.setAttribute("id", "report_table");
    thead.setAttribute("id", "report_table_head");
    tr.setAttribute("id", "report_table_head_tr");
    document.getElementById("data_table").appendChild(table);
    document.getElementById("report_table").appendChild(thead);
    document.getElementById("report_table_head").appendChild(tr);


    var th1 = document.createElement("TH");
    var x = document.createTextNode("Incident: ");
    th1.appendChild(x);
    document.getElementById("report_table_head_tr").appendChild(th1);

    var th2 = document.createElement("TH");
    x = document.createTextNode("#0000" + raw_data[current_report].pID);
    th2.appendChild(x);
    document.getElementById("report_table_head_tr").appendChild(th2);



    $(report_table).addClass("table table-hover");
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
    for (var i = 0; i < raw_data.length; i++) {
        var object = document.getElementById("" + i);
        $(object).removeClass("active");
    }
    $(obj).addClass("active");
    update_table();
}