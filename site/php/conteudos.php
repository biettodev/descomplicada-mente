<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge"/>
	<title>PHP project</title>
	
	<link rel="stylesheet"  href="../assets/css/style3.css"/>
	<link rel="stylesheet"  href="../assets/css/responsive.css"/>
	<script src="https://kit.fontawesome.com/3c8c3475df.js" crossorigin="anonymous"></script>
	
  </head>
  <body>
	
	<?php 
		session_start();
		if(!isset($_SESSION["autenticado"]))
		{
			header("Location: ../login.html");
		}
		include_once "../funcoes/conexao.php";
		include_once "../funcoes/model_users.php";
		// include_once "../funcoes/funcoes.php";
		
		$myemail = $_SESSION["email_user"]; //Obtém o o login do usuário
		$mypass = $_SESSION["pass_user"]; //Obtém a senha
			
	?>
	<div id="interface">
		
	
	<?php 
		
		$dados_user = get_dados_usuario($myemail, $mypass); //Chamada a função que que usa os dados do usuário em um array
		
		if(count($dados_user) == 0){ //Verifica se os dados existem
			echo "Desculpe! Não foram encontrados os dados desse usuário";
		}else{
			foreach($dados_user as $dados){
				
				echo "<h3>Bem vindo(a) à seção de conteúdos, {$dados["user_name"]}!</h3>";
				$_SESSION["id_user"] = $dados["user_id"];
				echo $_SESSION["id_user"];
			}
		}
			
		?>	
		
		<div id="content-container">
			
			<ul id="content-list">
				<li>
					<a class="content-type" href="contents/movies.php">
						<span>
							<i class="fas fa-film" ></i>
						</span>
						Filmes						
					</a>
				</li>
				
				<li>
					<a class="content-type" href="contents/channels.php">
						<span>
							<i class="fas fa-video" ></i>
						</span>
						Canais
					</a>
				</li>
				
				<li>
					<a class="content-type" href="contents/articles.php">
						<span>
							<i class="fas fa-newspaper" ></i>
						</span>
						Artigos
					</a>
				</li>
				
				<li>
					<a class="content-type"  href="contents/books.php">
						<span>
							<i class="fas fa-book" ></i>
						</span>
						Livros
					</a>
				</li>
			</ul>
		</div>		
		
		<a href="deslogar.php">Sair</a>
	</div>
	
  </body>
</html>

<?php
	

?>