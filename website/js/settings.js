function sensor_on_click(this_object) {
    var id = this_object.id;
    document.getElementById("save_message").innerHTML = "";


    if (id === "1"){
        document.getElementById("form_title").innerHTML = "Kitchen - Food Fridge:";
        document.getElementById('min').placeholder='2';
        document.getElementById('max').placeholder='3';

        $('#sensitivity').val("1min");
        $('#notify').val("user@TempSpace.com");



    }
    else if (id === "2"){
        document.getElementById("form_title").innerHTML = "Kitchen - Drinks Fridge:";
        document.getElementById('min').placeholder='3';
        document.getElementById('max').placeholder='4';
        $('#sensitivity').val("4hr");
        $('#notify').val("kieran@interns2017.com");

    }
    else if (id === "3"){
        document.getElementById("form_title").innerHTML = "Kitchen - Ambient Temperature:";
        document.getElementById('min').placeholder='5';
        document.getElementById('max').placeholder='8';
        $('#sensitivity').val("2hr");
        $('#notify').val("don@interns2017.com");

    }
    else {
        document.getElementById("form_title").innerHTML = "New Sensor:";
        document.getElementById('min').placeholder='4';
        document.getElementById('max').placeholder='6';
        $('#sensitivity').val("30min");
        $('#notify').val("chris@interns2017.com");

    }

}

function save_btn_click() {
    document.getElementById("save_message").innerHTML = '<div class="alert alert-primary alert-dismissible fade show" role="alert">\n' +
        '                    <strong>Saved</strong> *but not really\n' +
        '                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n' +
        '                        <span aria-hidden="true">&times;</span>\n' +
        '                    </button>\n' +
        '                </div>';
}