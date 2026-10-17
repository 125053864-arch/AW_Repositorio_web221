<?php

function conectar(){
    $host="localhost";
    $user="root";
    $pass="";


/* Base de datos */ 
$db="aw221";

$con=mysqli_connect($host,$user,$pass);

mysqli_select_db($con, $db);

return $con;



}

?>