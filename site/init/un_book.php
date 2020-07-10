<?php

	session_start();
	if(!isset($_SESSION["autenticado"]))
	{
		header("Location: ../login.html");
	}
	sleep(1);
	include_once "../funcoes/conexao.php";
	include_once "../funcoes/model_books.php";
	$id_book = (int)$_POST['id_book'];
	$id_user = (int)$_POST['id_user'];

	if(un_like($id_book, $id_user)){
		echo 'sucesso';
	}else{
		echo 'erro';
	}


?>