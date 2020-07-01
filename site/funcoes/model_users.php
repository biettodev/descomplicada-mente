<?php
function get_dados_usuario($email, $pass){
		$dados = array();
		
		$selecionar = mysql_query("SELECT `id_usuario`, `nome`, `email`, `senha` FROM `usuarios` WHERE `email` = '$email' AND `senha` = '$pass'");
		
		while($row = mysql_fetch_object($selecionar)){
			$dados[] = array(
				'user_id' => $row->id_usuario,
				'user_name' => $row->nome,
				'user_email' => $row->email,
				'user_pass' => $row->senha
			);
		}
		
		return $dados;
	}

function post_new_user($name, $email, $pass){
	
	//Registros
	$record = "INSERT INTO `usuarios` (nome, email, senha) VALUES('$name', '$email', '$pass')";
	$result = mysql_query($record);
	if($record){
		return true;
	}else{
		return false;
	}
}

?>