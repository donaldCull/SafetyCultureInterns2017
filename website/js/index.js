test_dic = {
    "Report_1":{
        "Sensor_1":{"Monday":[1.2,3.7,4.3,5.5], "Tuesday":[1.2,3.7,4.3,5.5], "Wednsday":[1.2,3.7,4.3,5.5], "Thursday":[1.2,3.7,4.3,5.5], "Friday":[1.2,3.7,4.3,5.5], "Saturday":[1.2,3.7,4.3,5.5], "Sunday":[1.2,3.7,4.3,5.5]},
        "Sensor_2":{"Monday":[1.2,3.7,4.3,5.5], "Tuesday":[1.2,3.7,4.3,5.5], "Wednsday":[1.2,3.7,4.3,5.5], "Thursday":[1.2,3.7,4.3,5.5], "Friday":[1.2,3.7,4.3,5.5], "Saturday":[1.2,3.7,4.3,5.5], "Sunday":[1.2,3.7,4.3,5.5]},
        "Sensor_3":{"Monday":[1.2,3.7,4.3,5.5], "Tuesday":[1.2,3.7,4.3,5.5], "Wednsday":[1.2,3.7,4.3,5.5], "Thursday":[1.2,3.7,4.3,5.5], "Friday":[1.2,3.7,4.3,5.5], "Saturday":[1.2,3.7,4.3,5.5], "Sunday":[1.2,3.7,4.3,5.5]},
    }

};


window.onload = function start() {
test()

};


function test() {
    document.getElementById("test_output").innerHTML = test_dic.Sensor_1.Report_3.Saturday[0];

}