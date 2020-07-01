<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge"/>
	<title>PHP project</title>
	<link rel="stylesheet"  href="css/style4.css"/>
	<link rel="stylesheet"  href="css/content.css"/>
	<link rel="stylesheet"  href="css/responsive.css"/>
	<script src="https://kit.fontawesome.com/3c8c3475df.js" crossorigin="anonymous"></script>
	
  </head>
  <body>
  
	// <?php
		// session_start();
		// if(!isset($_SESSION["autenticado"]))
		// {
			// header("Location: ./login.html");
		// }
		// include_once "../descomplicada-mente/funcoes/conexao.php";
		// include_once "./src/controllers/admin_controller.php";
		// include_once "./src/controllers/filme_controller.php";
		
		// $myid = $_SESSION["admin"]; //Obtém o o login do usuário
		// $mypass = $_SESSION["pass"]; //Obtém a senha
		
		// $dados_admin = get_dados_admin($myid, $mypass); //Chamada a função que que usa os dados do administrador em um array
		
		// if(count($dados_admin) == 0){ //Verifica se os dados existem
			// echo "Desculpe! Não foram encontrados os dados desse usuário";
		// }else{
			// foreach($dados_admin as $dados){
				
	// ?>
	<div id="interface">
		
		<h1>Bem Vindo, 
		</br>
	<?php  
			echo $dados["nome"];
			$_SESSION["id_admnistrador"] = $dados["admin_id"];
			} 
		}
	?>
		</h1>
		
		<div id="container-admin">
			
			<ul id="content-list">
				<li>
					<button class="button" onclick="alertar()" id="movies">
						<span>
							<i class="fas fa-film" ></i>
						</span>
						Filmes						
					</button>
				</li>
				
				<li>
					<button class="button" id="channels">
						<span>
							<i class="fas fa-video" ></i>
						</span>
						Canais
					</button>
				</li>
				
				<li>
					<button class="button" id="anticles">
						<span>
							<i class="fas fa-newspaper" ></i>
						</span>
						Artigos
					</button>
				</li>
				
				<li>
					<button class="button" id="books">
						<span>
							<i class="fas fa-book" ></i>
						</span>
						Livros
					</button>
				</li>
			</ul>
		</div>		
		
		<form id="content-form" class="hide" action="movie.php" method="post">
			<fieldset>
				<div class="field">
					<label for="title">Título do filme:</label>
					<input type="text" name="title" placeholder="Título" />
				</div>
				
				<div class="field">
					<label for="description">Sinópse:</label>
					<textarea name="description">
					</textarea>
				</div>
				
				<div class="field">
					<label for="author">Autor do filme:</label>
					<input type="text" name="author" placeholder="Autor" />
				</div>
			</fieldset>
			<div class="dialog">
				<button type="submit" id="addMovie">Adicionar</button>
				<button id="close">Cancelar</button>
				
			</div>
		</form>
		<a href="./src/utils/deslogar.php">Sair</a>
	</div>
	
	<script src="./js/scripts.js">
  </body>
</html>

<?php
	
	/*
	<form method="post" enctype="multipart/form-data">
				
				<button type="submit" class="button" id="adiciona">Adicionar</button>
				
				<button onclick="formDeletar()" class="button" id="remove">Remover</button>
				
				<input type="hidden" name="enviar" value="send" />
				
			</form>
	*/

?>