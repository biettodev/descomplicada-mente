<?php
	session_start();
	if(!isset($_SESSION["autenticado"]))
	{
		header("Location: ../login.html");
	}
	include_once "../funcoes/conexao.php";
	include_once "../funcoes/model_movies.php";
	$id_movie = (int)$_POST["id_movie"];
	$likes_count = return_likes($id_movie);
	echo $likes_count;
?>