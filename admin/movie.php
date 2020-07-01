<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge"/>
	<title>PHP project</title>
	<link rel="stylesheet"  href="css/style.css"/>
	<link rel="stylesheet"  href="css/content.css"/>
	<link rel="stylesheet"  href="css/responsive.css"/>
  </head>
  <body>
  
	<?php
		
		include_once "../descomplicada-mente/funcoes/conexao.php";
				
	?>
	<div id="interface">
		
		<div id="container-admin">
	<?php		
		
		$title = $_POST["title"];
		$desciption = $_POST["description"];
		$author = $_POST["author"];
		if(!empty($title)){
			echo "<h1>Dados do filme configurado</h1>";
			echo "<h2>{$title}</h2>";
		}else{
			echo "Algum dado não foi devidamente configurado";
		}
			
	?>
		</div>		
		<a href="./src/utils/deslogar.php" class="button">Sair</a>
		<a href="./index.php" class="button">Voltar</a>
	</div>
	
	
	<script src="https://kit.fontawesome.com/3c8c3475df.js" crossorigin="anonymous"></script>
  </body>
</html>

