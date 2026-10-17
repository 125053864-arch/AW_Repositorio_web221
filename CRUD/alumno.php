<?php

include("conexion.php");

$con = conectar();

$sql = "SELECT * from alumnos";

$query = mysqli_query($con,$sql);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Listar alumnos</title>
</head>
<body>
    <h1>Tabla alumnos</h1>

    <table border="2">
        <thead>
            <tr>
                <th>ID</th>
                <th>MATRICULA</th>
                <th>NOMBRE</th>
                <th>APELLIDO PATERNO</th>
                <th>APELLIDO MATERNO</th>
                <th>EDAD</th>
                <th>ACCIONES</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>125053864</td>
                <td>alvaro</td>
                <td>castro</td>
                <td>ortega</td>
                <td>30</td>
                <td>Editar Eliminalr</td>
            </tr>
        </tbody>
    </table>
    
</body>
</html>

