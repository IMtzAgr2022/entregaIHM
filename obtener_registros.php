<?php
// Realiza la conexión a la base de datos


$servername = "localhost";
$username = "userAcceso";
$password = "userAcceso";
$dbname = "Acceso";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Error de conexión a la base de datos: " . $conn->connect_error);
}

// Consulta los registros en la base de datos
$sql = "SELECT * FROM usuarios";
$result = $conn->query($sql);

$registros = array();

if ($result->num_rows > 0) {
    // Recorre los resultados de la consulta y agrega los registros al array
    while ($row = $result->fetch_assoc()) {
        $registro = array(
            "noCuenta" => $row["noCuenta"],
            "nombres" => $row["nombres"],
            "apellidoPaterno" => $row["apellidoPaterno"],
            "apellidoMaterno" => $row["apellidoMaterno"],
            "genero" => $row["genero"],
            "tipoUsuario" => $row["tipoUsuario"],
            "idTarjeta" => $row["idTarjeta"],
            "idHuella" => $row["idHuella"]
        );
        $registros[] = $registro;
    }
}

// Cierra la conexión a la base de datos
$conn->close();

// Devuelve los registros como respuesta en formato JSON
header("Content-Type: application/json");
echo json_encode($registros);
?>