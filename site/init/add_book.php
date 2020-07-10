<?php
	session_start();
	if(!isset($_SESSION["autenticado"]))
	{
		header("Location: ../login.html");
	}
	sleep(2);
	include_once "../funcoes/conexao.php";
	include_once "../funcoes/model_books.php";
	$id_book = (int)$_POST["id_book"];
	$id_user = (int)$_SESSION["id_user"];
	
	if(!verify_clicked($id_book, $id_user)){
		if(adicionar_like($id_book, $id_user)){
			echo "sucesso";
			
		}else{
			echo "erro";
		}
	}else{
		echo "erro";
	}
?>