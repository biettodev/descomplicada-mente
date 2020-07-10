function add_like(book_id){
	$('#livro'+book_id+'_like').html('<img src="../../assets/images/loading.gif" />');
	
	$.post('../../init/add_book.php', {id_book:book_id}, function(dados){
		if(dados == 'sucesso'){
			alert("O conteúdo foi adicionado!")
			get_like(book_id);
			location.href="../../php/contents/books.php";
		}else{
			alert("Você já votou neste livro de valor: "+book_id);
			location.href="../../php/contents/books.php";
		}
	});
}

function get_like(book_id){
	$.post('../../init/get_book.php', {id_book:book_id}, function(valor){
		$('#livro_'+book_id+'_like').text(valor); //Este é o valor da quantidade de likes dados no post
	});
}
function un_like(book_id, user_id){
	$('#livro'+book_id+'_like').html('<img src="../../assets/images/loading.gif" />');

	$.post('../../init/un_book.php', {id_book:book_id, id_user:user_id}, function(valor){
		if(valor == 'sucesso'){
			alert("O conteúdo foi removido!")
			location.href="../../php/contents/books.php"; 
		}else{
			alert("Desculpe, ocorreu algum erro: "+book_id);
			location.href="../../php/contents/books.php";
		}
	});
}