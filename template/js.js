
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