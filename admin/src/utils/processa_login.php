<?php

	include_once "../models/conexao.php";
	include_once "../controllers/admin_controller.php";
	
	$admin_id = $_POST["idadmin"];
	$senha = $_POST["senha"];
	
	$dados_admin = get_dados_admin($admin_id, $senha);
	
	if(count($dados_admin) == 0){
		echo "Nenhum administrador correspondente";
		header("Location: ../../login.html");
	}
	else{
		
	}foreach($dados_admin as $dados){
		$_SESSION["id_administrador"] = $dados["admin_id"];
		if($_POST["idadmin"] == $dados["admin_id"] && $_POST["senha"] == $dados["senha"]){
			session_start();
			$_SESSION["autenticado"] = true;
			$_SESSION["admin"] = $dados["admin_id"];
			$_SESSION["pass"] = $dados["senha"];
		
			header("Location: ../../index.php");
		}else{
			echo "Dados inválidos";
			header("Location: ../../login.html");
		}
	}
	
	echo "$admin_id";
?>