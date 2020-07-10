<?php
	function get_movies(){
		$movies = array();
		
		$select = mysql_query("SELECT `id_filme`,`titulo`,`sinopse`, `autor`, `likes`, `url_thumb`, `usuario_like` FROM `filmes`");
		
		while($row = mysql_fetch_object($select)){
			$signedUser = (int)$_SESSION["id_user"];
			$mov_id = $row->id_filme;
			$verify = mysql_query("SELECT `like_id` FROM `movie_likes` WHERE user_id = '$signedUser' AND `movie_id` = '$mov_id'");
			$usr_liked = (mysql_num_rows($verify) == 0) ? '0' : '1';
			$movies[] = array(
				'movie_id' => $row->id_filme,
				'movie_title' => $row->titulo,
				'movie_description' => $row->sinopse,
				'movie_author' => $row->autor,
				'movie_likes' => $row->likes,
				'movie_thumb' => $row->url_thumb,
				'movie_user_liked' => $usr_liked
			);
		}
		
		return $movies;
	}
	
	function verify_clicked($movie_id, $user_id){
		$movie_id = (int)$movie_id; //Recupera o valor do ID do filme
		$user_id = (int)$user_id; //Recupera o valor do ID do usuário
		$verify = mysql_query("SELECT `like_id` FROM `movie_likes` WHERE `user_id` = '$user_id' AND movie_id = '$movie_id'");
		return (mysql_num_rows($verify) >= 1) ? true : false;
	}
	
	
	function adicionar_like($movie_id, $user_id){
		$movie_id = (int)$movie_id; //Recupera o valor do ID do filme
		$user_id = (int)$user_id; //Recupera o valor do ID do usuário
		$movie_likes_update = mysql_query("UPDATE `filmes` SET `likes` = likes+1 WHERE `id_filme` = '$movie_id'"); //Atualiza a quantidade de likes para o filme
		
		if($movie_likes_update){ //Verifica se foi atualizado
			$like_insert = mysql_query("INSERT INTO `movie_likes` (`user_id`, `movie_id`) VALUES ('$user_id','$movie_id')");
			if($like_insert){
				return true;	
			}else{
				return false;
			}
		}
	}
	
	function return_likes($movie_id){ //
		$movie_id = (int)$movie_id;
		$selecionar_num_likes = mysql_query("SELECT `likes` FROM `filmes` WHERE `id_movie` = '$movie_id'"); //Seleciona os likes da tabela filmes no ID do filme
		$fetch_likes = mysql_fetch_object($selecionar_num_likes);
		return $fetch_likes->likes;
	}
	
	function un_like($movie_id, $user_id){

		$delete = mysql_query("DELETE FROM `movie_likes` WHERE `user_id` = '$user_id' AND `movie_id` = '$movie_id'");
		if($delete){
			$update = mysql_query("UPDATE `filmes` SET `likes` = likes-1 WHERE `id_filme` = '$movie_id'");
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