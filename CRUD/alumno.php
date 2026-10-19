
<?php

include("conexion.php");

$con = conectar();

$sql = "SELECT * FROM alumnos";

$query = mysqli_query($con, $sql);

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
            <?php
            while ($row = mysqli_fetch_array($query)) {
            ?>

            <tr>
                <td><?php echo $row['id'] ?></td>
                <td><?php echo $row['matricula'] ?></td>
                <td><?php echo $row['nombre'] ?></td>
                <td><?php echo $row['apellido_p'] ?></td>
                <td><?php echo $row['apellido_m'] ?></td>
                <td><?php echo $row['edad'] ?></td>

                <td>
                    

                  <a href="editar.php?id=<?php echo $row['id']; ?>">Editar</a>
                  <br>
                  <a href="delete.php?id=<?php echo $row['id']; ?>">Eliminar</a>


                </td>
            </tr>

            <?php
            }
            ?>
        </tbody>
    </table>

    <h1>FORMULARIO</h1>

    <form action="insertar.php" method="POST">
        <input type="text" name="matricula" placeholder="Matricula">
        <input type="text" name="nombre" placeholder="Nombre(s)">
        <input type="text" name="apellido_p" placeholder="Apellido_p">
        <input type="text" name="apellido_m" placeholder="Apellido_m">
        <input type="text" name="edad" placeholder="Edad">
        <button type="submit">Guardar</button>
    </form>


</body>
</html>
