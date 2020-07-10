<?php
	session_start();
	if(!isset($_SESSION["autenticado"]))
	{
		header("Location: ../login.html");
	}
	include_once "../funcoes/conexao.php";
	include_once "../funcoes/model_books.php";
	$id_book = (int)$_POST["id_book"];
	$likes_count = return_likes($id_book);
	echo $likes_count;
?>