function add_like(movie_id){
	$('#filme_'+movie_id+'_like').html('<img src="../../assets/images/loading.gif" />');
	
	$.post('../../init/add_like.php', {id_movie:movie_id}, function(dados){
		if(dados == 'sucesso'){
			alert("O conteúdo foi adicionado!")
			get_like(movie_id);
			location.href="../../php/contents/movies.php";
		}else{
			alert("Você já votou neste filme de valor: "+movie_id);
			location.href="../../php/conteudos.php";
		}
	});
}

function get_like(movie_id){
	$.post('../../init/get_like.php', {id_movie:movie_id}, function(valor){
		$('#filme_'+movie_id+'_like').text(valor); //Este é o valor da quantidade de likes dados no post
	});
}
function un_like(movie_id, user_id){
	$('#filme_'+movie_id+'_like').html('<img src="../../assets/images/loading.gif" />');

	$.post('../../init/un_like.php', {id_movie:movie_id, id_user:user_id}, function(valor){
		if(valor == 'sucesso'){
			alert("O conteúdo foi removido!")
			location.href="../../php/contents/movies.php"; 
		}else{
			alert("Desculpe, ocorreu algum erro: "+movie_id);
			location.href="../../php/conteudos.php";
		}
	});
}