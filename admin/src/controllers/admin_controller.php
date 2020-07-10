<?php
	function get_admin_data($admin_id, $admin_pass){
		$dados = array();
		
		$selecionar = mysql_query("SELECT `id_admin`, `nome_admin`, `email_admin`, `senha_admin` FROM `admin` WHERE `id_admin` = '$admin_id' AND `senha_admin` = '$admin_pass'");
		
		while($row = mysql_fetch_object($selecionar)){
			$dados[] = array(
				'admin_id' => $row->id_admin,
				'admin_nome' => $row->nome_admin,
				'admin_email' => $row->email_admin,
				'admin_pass' => $row->senha_admin
			);
		}
		
		return $dados;
	}
	
	function post_new_admin($admin_id, $admin_name, $admin_email, $admin_pass){
		// $insert = ("INSERT INTO `admin`(`id_admin`, `nome_admin`, `email_admin`, `senha_admin`) VALUES ($admin_id, '$admin_name', '$admin_email', '$admin_pass')");
		// $insert = ("INSERT INTO `admin`(`id_admin`, `nome_admin`, `email_admin`, `senha_admin`) VALUES ('$admin_id', '$admin_name', '$admin_email', '$admin_pass')");
		$insert = mysql_query("INSERT INTO `admin`(`id_admin`, `nome_admin`, `email_admin`, `senha_admin`) VALUES ($admin_id, '$admin_name', '$admin_email', '$admin_pass')");
		if($insert){
			return true;
		}else{
			return false;
		}
	}
	
	// function delete_admin($admin_id, $admin_name){
		// $delete = ("");
	// }
?>