<?php
/**
 * Created by PhpStorm.
 * User: donald
 * Date: 30/11/2017
 * Time: 4:42 PM
 */
// get the q parameter from URL
include "inc/dbInfo.inc";

$q = $_REQUEST["q"];
$conn = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);

if (mysqli_connect_errno()) echo "Failed to connect to MySQL: " . mysqli_connect_error();
$sql = "SELECT * FROM Report WHERE Report_ID=$q";

//$result = mysqli_query($conn, $sql);

$results_array = array();
$result = $conn->query($sql);
while ($row = $result->fetch_assoc()){
    $results_array[] = $row;
}
$myJSON = json_encode($results_array);
echo $myJSON;