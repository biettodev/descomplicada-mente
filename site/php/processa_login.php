<?php
	include_once "../funcoes/conexao.php";
	include_once "../funcoes/model_users.php";

	$email = $_POST["email"];
	$pass = $_POST["pass"];
	
	// Chamada da função que realiza a consulta de login 
	$dados_user = get_dados_usuario($email, $pass);
	
	if(count($dados_user) == 0){
		echo "Nenhum usuário correspondente!";
		header("Location: ../login.html");
	}else{
		
	}foreach($dados_user as $dados){
		$_SESSION["id_user"] = $dados["usuario_id"];
		
		if($_POST["email"]==$dados["user_email"] && $_POST["pass"]==$dados["user_pass"]){
			session_start();
			$_SESSION["autenticado"] = true;
			$_SESSION["email_user"] = $_POST["email"];
			$_SESSION["pass_user"] = $_POST["pass"];
			
			
			header("Location: conteudos.php");
		}else{
			echo "Dados Inválidos!";
			header("Location: ../login.html");
		}
	}
?>