<?php
	
	$admin_id = rand(1, 9999999);
	$admin_name = $_POST["adminname"];
	$admin_email = $_POST["adminemail"];
	$admin_pass = $_POST["adminpass"];

?>

<!DOCTYPE html>
<html lang="pt-br">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<meta http-equiv="X-UA-Compatible" content="ie=edge"/>
		<link rel="stylesheet"  href="../../css/style.css"/>

		<link rel="stylesheet"  href="../../css/responsive.css"/>
		<title>PHP project</title>
		<script src="https://kit.fontawesome.com/3c8c3475df.js" crossorigin="anonymous"></script>
	</head>
	<body>
		<div id="interface">
	
<?php
	
	include_once("../models/conexao.php");
	include_once("../controllers/admin_controller.php");

	$create_admin = post_new_admin($admin_id, $admin_name, $admin_email, $admin_pass);
	
	if($create_admin){
		echo "<h1>Seu cadastro foi realizado com sucesso!</h1>";
		echo "<h2>Suas informações são:</h2>";
		// echo "<p>SEU ID PARA: {$admin_id}</p>";
		echo "<p>NOME: {$admin_id}</p>";
		echo "<p>NOME: {$admin_name}</p>";
		echo "<p>E-MAIL: {$admin_email}</p>";
		echo "<p>SUA SENHA PARA ACESSO: {$admin_pass}</p>";
		echo "<div class='dialog'><a href='../../login.html'>Confirmar e logar</a></div>";
	}else{
		echo "<h1>ERRO AO REALIZAR CADASTRO!</h1>";
	}
?>
			
		</div>
	</body>
</html>
