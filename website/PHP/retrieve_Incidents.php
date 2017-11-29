<?php
include "inc/dbInfo.inc";
/* Connect to MySQL and select the database. */

$connection = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);

if (mysqli_connect_errno()) echo "Failed to connect to MySQL: " . mysqli_connect_error();

$sql = "SELECT * FROM Incidents";
$result = $connection->query($sql);
$testvar = "";
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $testvar = $row["pID"];
    }
} else {
    echo "0 results";
}
$myJSON = '{ "name": ' . $testvar . ', "age":30, "city":"New York" }';


echo "myFunc(".$myJSON.");";





