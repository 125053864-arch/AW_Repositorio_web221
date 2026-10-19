<?php
include("conexion.php");

$con = conectar();
$id= $_GET['id'];

$sql = "SELECT * FROM alumnos WHERE id= '$id'";

$row = mysqli_fetch_array($query);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar alumno>
</head>
<body>

<h1>Editar alumno</h1>

<form action="actualizar.php" method= "POST">
    <input type= "hidden" name= "id" value= "<?php echo $row['id'];?>">

    <input type="text" name= "matricula" value="<?php echo $row['matricula'];?>" placeholder="Matricula">
    <input type="text" name= "nombre" value="<?php echo $row['nombre'];?>" placeholder="Nombre">
    <input type="text" name= "apellido_p" value="<?php echo $row['apellido_p'];?>" placeholder="Apellido paterno">
    <input type="text" name= "apellido_m" value="<?php echo $row['apellido_m'];?>" placeholder="Apellido materno">
    <input type="text" name= "edad" value="<?php echo $row['edad'];?>" placeholder="Edad">

    <button type="submit">actualizar</button>

</form>
    


    
</body>
</html>