<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge"/>
	<link rel="stylesheet"  href="css/style2.css"/>
	<title>PHP project</title>
  </head>
  <body>
	<div id="interface">
		<h1>Bem Vindo, 
			</br>(Nome)
		</h1>
		<div id="container-admin">
			
			
			<ul id="lista-filmes">
				<li>
					<button id="filmes" onclick="">Filmes</button>
				</li>
				
				<li>
					<button id="canais" onclick="">Canais</button>
				</li>
				
				<li>
					<button id="artigos" onclick="">Artigos</button>
				</li>
				
				<li>
					<button id="livros" onclick="">Livros</button>
				</li>
				
			</ul>
			
			<form method="post" action=".php">
				
					Título:<input id="titulo" type="text" name="titulo"/><br/>
					
					Sinopse:</br><textarea id="sinopse" name="sinopse">
					</textarea><br/>	
					
					Autor:<input id="autor" type="text" name="autor"/><br/>
					
			</form>
		</div>
		<div id="opcoes">
			<button type="submit">Adicionar</button>
			
			<button type="submit">Remover</button>
		</div>
	</div>
  </body>
</html>