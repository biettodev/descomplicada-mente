<?php
	function get_books(){
		$books = array();
		
		$select = mysql_query("SELECT `id_livro`,`titulo`,`sinopse`, `autor`, `likes`, `url_thumb` FROM `livros`");
		
		while($row = mysql_fetch_object($select)){
			$signedUser = (int)$_SESSION["id_user"];
			$boo_id = $row->id_livro;
			$verify = mysql_query("SELECT `like_id` FROM `book_likes` WHERE `user_id` = '$signedUser' AND `book_id` = '$boo_id'");
			$usr_liked = (mysql_num_rows($verify) == 0) ? '0' : '1';
			$books[] = array(
				'book_id' => $row->id_livro,
				'book_title' => $row->titulo,
				'book_description' => $row->sinopse,
				'book_author' => $row->autor,
				'book_likes' => $row->likes,
				'book_thumb' => $row->url_thumb,
				'book_user_liked' => $usr_liked
			);
		}
		
		return $books;
	}
	
	function verify_clicked($book_id, $user_id){
		$book_id = (int)$book_id; //Recupera o valor do ID do filme
		$user_id = (int)$user_id; //Recupera o valor do ID do usuário
		$verify = mysql_query("SELECT `like_id` FROM `book_likes` WHERE `user_id` = '$user_id' AND book_id = '$book_id'");
		return (mysql_num_rows($verify) >= 1) ? true : false;
	}
	
	
	function adicionar_like($book_id, $user_id){
		$book_id = (int)$book_id; //Recupera o valor do ID do filme
		$user_id = (int)$user_id; //Recupera o valor do ID do usuário
		$movie_likes_update = mysql_query("UPDATE `livros` SET `likes` = likes+1 WHERE `id_livro` = '$book_id'"); //Atualiza a quantidade de likes para o filme
		
		if($movie_likes_update){ //Verifica se foi atualizado
			$like_insert = mysql_query("INSERT INTO `book_likes` (`user_id`, `book_id`) VALUES ('$user_id','$book_id')");
			if($like_insert){
				return true;	
			}else{
				return false;
			}
		}
	}
	
	function return_likes($book_id){ //
		$book_id = (int)$book_id;
		$selecionar_num_likes = mysql_query("SELECT `likes` FROM `livros` WHERE `id_livro` = '$book_id'"); //Seleciona os likes da tabela livros no ID do filme
		$fetch_likes = mysql_fetch_object($selecionar_num_likes);
		return $fetch_likes->likes;
	}
	
	function un_like($book_id, $user_id){

		$delete = mysql_query("DELETE FROM `book_likes` WHERE `user_id` = '$user_id' AND `book_id` = '$book_id'");
		if($delete){
			$update = mysql_query("UPDATE `livros` SET `likes` = likes-1 WHERE `id_livro` = '$book_id'");
			if($update){
				return true;
			}else{
				return false;
			}
		}else{
			return false;
		}
	}
?>