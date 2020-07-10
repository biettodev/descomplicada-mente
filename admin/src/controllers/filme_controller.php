<?php
	function post_new_movie($imagepath, $titulo, $sinopse, $autor){
		
		$inserir = mysql_query("INSERT INTO `filmes`(`titulo`, `sinopse`, `autor`) VALUES ('$titulo', '$sinopse', '$autor')");
		
		if($inserir){
			return true;
		}else{
			return false;
		}
	}
	
	function delete($titulo, $id_filme){
		
		$deletar = mysql_query("DELETE `ds`.`filmes` WHERE `filmes`.`filme_id` = '$id_filme'");
		
		if($deletar){
			return true;
		}else{
			return false;
		}
		
	}

?>