<?php
	$host = 'localhost';
	$user = 'root';
	$pass = 'usbw';
	$banco = 'dm';
	
	$conectar = mysql_connect($host, $user, $pass);
	if($conectar){
		mysql_select_db($banco);
	}else{
		echo "Erro com o banco";
	}
?>