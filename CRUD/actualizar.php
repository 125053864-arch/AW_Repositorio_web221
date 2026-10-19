<?php

include("conexion.php");

$con = conectar();

$id = $_POST['id'];
$matricula = $_POST['matricula'];
$id = $_POST['nombre'];
$id = $_POST['apellido_p'];
$id = $_POST['apellido_m'];
$id = $_POST['edad'];

$sql = "UPDATE alumnos SET
matricula='$matricula',
nombre= '$nombre',
apellido_p='$apellido_p',
apellido_m='$apellido_m',
edad='$edad'
WHERE id= '$id'";

$query = mysqli_query($con,$sql);

if ($query) {
    header("Location: alumnos.php");
    exit();

}else {
    echo "Erroral actualizar los datos";
}
?>