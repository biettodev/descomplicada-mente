<?php
	function get_dados_admin($admin_id, $senha){
		$dados = array();
		
		$selecionar = mysql_query("SELECT `id_admin`, `nome`, `email`, `senha` FROM `admins` WHERE `id_admin` = '$admin_id' AND `senha` = '$senha'");
		
		while($row = mysql_fetch_object($selecionar)){
			$dados[] = array(
				'admin_id' => $row->id_admin,
				'nome' => $row->nome,
				'email' => $row->email,
				'senha' => $row->senha
			);
		}
		
		return $dados;
	}
?>