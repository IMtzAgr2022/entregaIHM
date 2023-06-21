<?php
// Establecer la conexión a la base de datos
$servername = "localhost";
$usernameDB = "userAcceso";
$passwordDB = "userAcceso";
$dbname = "Acceso";

// Crear la conexión
$conn = new mysqli($servername, $usernameDB, $passwordDB, $dbname);

// Verificar si hay errores en la conexión
if ($conn->connect_error) {
    die("Error de conexión a la base de datos: " . $conn->connect_error);
}

// Obtenemos los datos ingresados por el usuario
$username = $_GET['username'];
$password = $_GET['password'];

// Escapar los datos para evitar inyección SQL
$username = $conn->real_escape_string($username);
$password = $conn->real_escape_string($password);

// Realizar la consulta a la base de datos
$sql = "SELECT * FROM administrador WHERE userLogin = '$username' AND passwdLogin = '$password'";
$result = $conn->query($sql);

// Verificar si se encontró un registro coincidente
if ($result->num_rows == 1) {
    // Los datos son correctos, redirigir al usuario a la página del administrador
    header('Location: pagina_administrador.html');
    exit(); // Importante: Salir del script para evitar que se siga ejecutando
} else {
    // Los datos son incorrectos, puedes mostrar un mensaje de error o redirigir a otra página
    //echo 'Usuario o contraseña incorrectos';
    //echo '<script>alert("Usuario o contraseña incorrectos.");</script>';
    //header('Location: pagina_login.html');
    //echo '<script>alert("Usuario o contraseña incorrectos. Digite nuevamente");</script>';
    header('Location: pagina_login.html?error=1');
    exit();
    //echo 'Usuario o contraseña incorrectos';
}

// Cerrar la conexión a la base de datos
$conn->close();
?>
