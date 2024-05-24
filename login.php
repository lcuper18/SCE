<!-- login.php -->
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header">Login</div>
                    <div class="card-body">
                        <form action="login.php" method="post">
                            <div class="form-group">
                                <label for="cedula">Cédula</label>
                                <input type="text" class="form-control" id="cedula" name="cedula" required>
                            </div>
                            <div class="form-group">
                                <label for="password">Contraseña</label>
                                <input type="password" class="form-control" id="password" name="password" required>
                            </div>
                            <button type="submit" class="btn btn-primary">Iniciar Sesión</button>
                        </form>
                        <?php
                        // Conexión a la base de datos y validación de credenciales
                        if ($_SERVER["REQUEST_METHOD"] == "POST") {
                            $cedula = $_POST["cedula"];
                            $password = $_POST["password"];

                            // Código para conectar a la base de datos y validar las credenciales
                            $conn = new mysqli("monorail.proxy.rlwy.net", "root", "ywsSqojfvtsIjQUqILlvNAmnBbBsyDqB", "SCE");
                            if ($conn->connect_error) {
                                die("Connection failed: " . $conn->connect_error);
                            }

                            $sql = "SELECT * FROM tutores WHERE cedula = '$cedula' AND password = '$password'";
                            $result = $conn->query($sql);

                            if ($result->num_rows > 0) {
                                // Credenciales válidas, redirigir al usuario a la página principal
                                header("Location: menu.php");
                                exit();
                            } else {
                                echo "<div class='alert alert-danger'>Credenciales inválidas</div>";
                            }

                            $conn->close();
                        }
                        ?>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>