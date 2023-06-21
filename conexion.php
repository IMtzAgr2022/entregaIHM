<?php
// Configuración de la conexión a la base de datos
$host = "localhost";
$usuario = "root";
$password = "";
$baseDatos = "Acceso";

try {
    // Crear la conexión utilizando la extensión PDO
    $conexion = new PDO("mysql:host=$host;dbname=$baseDatos", $usuario, $password);

    // Configurar el modo de error para lanzar excepciones en caso de error
    $conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Obtener los datos del formulario enviados mediante el método GET
    $noCuenta = $_GET['noCuenta'];
    $nombres = $_GET['nombres'];
    $apellidoPaterno = $_GET['apellidoPaterno'];
    $apellidoMaterno = $_GET['apellidoMaterno'];
    $genero = $_GET['genero'];
    $tipoUsuario = $_GET['tipoUsuario'];
    $idTarjeta = $_GET['idTarjeta'];
    $idHuella = $_GET['idHuella'];

    // Preparar la consulta SQL de inserción
    $consulta = $conexion->prepare("INSERT INTO usuarios (nocuenta, nombres, apellidoPaterno, apellidoMaterno, genero, tipoUsuario, idTarjeta, idHuella) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");

    // Ejecutar la consulta con los valores de los parámetros
    $consulta->execute([$noCuenta, $nombres, $apellidoPaterno, $apellidoMaterno, $genero, $tipoUsuario, $idTarjeta, $idHuella]);

    // Redireccionar a la página de éxito o mostrar un mensaje de éxito
    header("Location: pagina_administrador.html");
    exit();
} catch (PDOException $e) {
    // Mostrar un mensaje de error en caso de excepción
    die("Error de conexión: " . $e->getMessage());
}
?>
