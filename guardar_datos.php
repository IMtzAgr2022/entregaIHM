<?php
// Establecer la conexión con la base de datos (actualiza los valores según tu configuración)
session_start();
$host = "localhost";
$dbname = "Acceso";
$username = "userAcceso";
$password = "userAcceso";
$dsn = "mysql:host=$host;dbname=$dbname;charset=utf8mb4";

try {
    $pdo = new PDO($dsn, $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Error de conexión: " . $e->getMessage());
}

// Obtener los datos del formulario usando el método POST
$noCuenta = $_POST['noCuenta'];
$nombres = $_POST['nombres'];
$apellidoPaterno = $_POST['apellidoPaterno'];
$apellidoMaterno = $_POST['apellidoMaterno'];
$genero = $_POST['genero'];
$tipoUsuario = $_POST['tipoUsuario'];
$idTarjeta = $_POST['idTarjeta'];
$idHuella = $_POST['idHuella'];

// Función para validar registros duplicados
function validarRegistroDuplicado($pdo, $noCuenta, $idTarjeta, $idHuella) {
    $sql = "SELECT COUNT(*) AS count FROM Usuarios WHERE noCuenta = ? OR idTarjeta = ? OR idHuella = ?";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$noCuenta, $idTarjeta, $idHuella]);
    $result = $stmt->fetch(PDO::FETCH_ASSOC);
    $count = $result['count'];
    return $count > 0;
}

// Validar registros duplicados
if (validarRegistroDuplicado($pdo, $noCuenta, $idTarjeta, $idHuella)) {
    $_SESSION['message_type'] = "error";
    $_SESSION['error_message'] = "Ya existe un registro con el mismo número de cuenta, tarjeta o huella.";
    header('Location: index.html?error=1');
    exit();
} else {
    // Preparar la consulta SQL para insertar los datos
    $sql = "INSERT INTO Usuarios (noCuenta, nombres, apellidoPaterno, apellidoMaterno, genero, tipoUsuario, idTarjeta, idHuella) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
    
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute([$noCuenta, $nombres, $apellidoPaterno, $apellidoMaterno, $genero, $tipoUsuario, $idTarjeta, $idHuella]);
        
        header('Location: index.html');
        exit();
    } catch (PDOException $e) {
        header('Location: index.html?error=1');
        exit();
    }
}
?>
