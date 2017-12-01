<?php
include "inc/dbInfo.inc";
/* Connect to MySQL and select the database. */

$conn = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);

if (mysqli_connect_errno()) echo "Failed to connect to MySQL: " . mysqli_connect_error();
$sql = "SELECT report_date FROM Report";

$result = mysqli_query($conn, $sql);

$results_array = array();
$result = $conn->query($sql);
while ($row = $result->fetch_assoc()){
    $results_array[] = $row;
}
$myJSON = json_encode($results_array);
echo $myJSON;
