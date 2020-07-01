<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge"/>
	<title>PHP project</title>
	<style>
		body{
			font: normal 12px Arial;
			text-align: center;
		}
		fieldset{
			width: 500px;
			margin: 5px auto 3px auto;
			font: bold 15px Helvetica;
		}
		input{
			padding: 10px;
			margin: 10px;
			border-style: none;
			border-radius: 3px;
		}
	</style>
  </head>
  <body>
	<fieldset>
		<?php
			include_once "../funcoes/conexao.php";
			include_once "../funcoes/model_users.php";
			
			$name = $_GET['name'];
			$email = $_GET['email'];
			$pass = $_GET['password'];
			
			$create_result = post_new_user($name, $email, $pass);
			
			if($create_result){
				echo "Seu cadastro foi realizado com sucesso! </br>";
			}else{
				echo "Erro!</br>";
			}
		?>
		<a href="../cadastro.html">Voltar</a>
		<a href="../login.html">Login</a>
	</fieldset>
  </body>
</html>