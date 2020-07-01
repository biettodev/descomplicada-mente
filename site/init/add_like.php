<?php
	session_start();
	if(!isset($_SESSION["autenticado"]))
	{
		header("Location: ../login.html");
	}
	sleep(2);
	include_once "../funcoes/conexao.php";
	include_once "../funcoes/model_movies.php";
	$id_movie = (int)$_POST["id_movie"];
	$id_user = (int)$_SESSION["id_user"];
	
	if(!verify_clicked($id_movie, $id_user)){
		if(adicionar_like($id_movie, $id_user)){
			echo "sucesso";
			
		}else{
			echo "erro";
		}
	}else{
		echo "erro";
	}
?>