<!DOCTYPE HTML>
<html>
	<head>
		<title>Conteúdos - Filmes</title>
		<script type="text/javascript" src="../../js/jquery.js"></script>
		<script type="text/javascript" src="../../js/movies_func.js"></script>
		<script src="https://code.iconify.design/1/1.0.6/iconify.min.js"></script>
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!-- <link rel="stylesheet" href="../../assets/css/main.css" /> -->
		<link rel="stylesheet" href="../../assets/css/style3.css" />
		<link rel="stylesheet" href="../../assets/css/content.css" />
		<link rel="stylesheet" href="../../assets/css/responsive.css" />
	</head>
	</head>
	<body>
	
			<?php 
				include_once "../../funcoes/conexao.php";
				include_once "../../funcoes/model_users.php";
				include_once "../../funcoes/model_movies.php";
				session_start();
				if(!isset($_SESSION["autenticado"]))
				{
					header("Location: ../login.html");
				}
				
				$myemail = $_SESSION["email_user"]; //Obtém o o login do usuário
				$mypass = $_SESSION["pass_user"]; //Obtém a senha
				
			?>
		
		<!-- Wrapper -->
		<div id="wrapper">
			
			<!-- Main -->
			<section id="main">

				<!-- fotos -->
				<section class="thumbnails">
				<div id="action">
					<a href="../deslogar.php">Sair</a>
					<a href="../conteudos.php">Voltar</a>
				</div>
				
				<ul>
						
	<?php 
			//Chamada da função que seleciona todos os filmes do Banco de Dados
			$resultados = get_movies(); 
			
			if(count($resultados) == 0){ //Verifica se a quantidade de conteúdos é igual a zero
				echo 'Desculpe, mais não foram encontrados filmes';
			}else{
				
				//Repetição para mostrar todos os filmes do Banco
				foreach($resultados as $movies){ 
	?>				
				<li>
	<?php			
					//Adiciona a imagem
					echo "<p><img src='../../assets/images/thumbs/filmes/{$movies["movie_thumb"]}.jpg' alt'{$movies["movie_title"]}'/></p>"; 
	?>
				
	<?php	
				//Adiciona o título do filme
				echo "<p><h1> {$movies["movie_title"]}</h1></p>"; 
				
				echo "<p><h1> {$movies["movie_description"]}...</h1></p>";
				
				echo "<p><h1> Dirigido por:{$movies["movie_author"]}...</h1></p>";
	?>
					
	<?php 
					if($movies['movie_user_liked'] == 0){
	?>
				<p>
					<a href="#" class="like" onclick="javascript:add_like(<?php echo $movies["movie_id"];?>);">Adicionar</a> 
		
	<?php  
					}else{
	?>
					<a href="#" class="like" onclick="javascript:un_like(<?php echo $movies["movie_id"];?>, <?php echo $_SESSION["id_user"];?>);">Unlike</a> 
		
	<?php 
					} 
	
					echo "<p class='info'><span id='filme_{$movies["movie_id"]}_like'><strong>{$movies["movie_likes"]}</strong></span><span>gostaram disto!</span></p>";
	?>				
	
	
				</li>
	<?php
				}
			
			}
	?>
				</ul>
				</section>
			</section>

		<!-- rodapé -->
			<footer id="footer">
					<h1>Disponíveis em:</h1> 
					<ul class="icons">
						<li>
							<img src="../../assets/images/netflix.png" alt="" />
						</li>
						<li>
							<img src="../../assets/images/youtube.png" alt="" />
						</li>
						<li>
							<img src="../../assets/images/amazon.jpg" alt="" />
						</li>
					</ul>
			</footer>
		</div>
	</body>
</html>