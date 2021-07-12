
var i = 5;//время в сек.

function time(){

	document.getElementById("time").innerHTML = i;//визуальный счетчик

	i--;//уменьшение счетчика

	if (i < 0) location.href = "login";//редирект

	}

	time();

	setInterval(time, 1000);


