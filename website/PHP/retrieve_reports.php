<?php
/**
 * Created by PhpStorm.
 * User: donald
 * Date: 30/11/2017
 * Time: 4:42 PM
 */
// get the q parameter from URL
//$q = $_REQUEST["q"];
$conn = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);

if (mysqli_connect_errno()) echo "Failed to connect to MySQL: " . mysqli_connect_error();
$sql = "SELECT * FROM Report WHERE pID=1";

$result = mysqli_query($conn, $sql);
$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
mysqli_free_result($result);

$myJSON = json_encode($row);
echo $myJSON;
