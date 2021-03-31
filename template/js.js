
//let res = 'a';
//document.getElementById("someRes").innerHTML = res;


document.querySelector("#resButton").onclick = function(){
	// s = document.getElementById('in0');
	let sa = document.querySelector("#in0").value;
	let s = document.querySelector("#in1").value;
	Number.parseInt(sa);
	Number.parseInt(s);
	res = sa + s;
    document.getElementById("someRes").innerHTML = res;
	//alert(res);
};

function sendMessage () {
		let xhrObj = new XMLHttpRequest();
		let text = textArea.value;
		let name = userName.value;
		console.log(text);
		//console.log(name);
		xhrObj.open('GET', 'http://chat21.std-400.ist.mospolytech.ru/add.ajax.php?name=+name+&text=+text');
		xhrObj.send();
		if(xhrObj.response){
			let result = JSON.parse(xhrObj.response);
			console.log(result);
			
		}
		/*
		if (xhrObj.status != 200) {
		// обработать ошибку
			//alert( xhrObj.status + ': ' + xhrObj.statusText ); // пример вывода: 404: Not Found
		} else {
		// вывести результат
			//alert( xhrObj.responseText ); // responseText -- текст ответа.
		}
		*/
		
		
};

let button1 = document.getElementById('sendButton');
let userName = document.getElementById('vvName');
let textArea = document.getElementById('vvText');
//sendButton.onclick =  sendMessage();
button1.addEventListener('click',sendMessage);


/*

#	alert(firstChislo);
#dontWork.onclick = function() {
#    alert('Не работаетпока что. Брат, прости(');
#  };

function getData() {
	//let firstChislo = document.getElementByID("in0")value;
	//let secondChislo = document.getElementByID("in1")value;
	alert("firstChislo");
	
}
*/