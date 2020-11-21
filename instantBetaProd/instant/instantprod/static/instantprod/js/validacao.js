function ClassAddValid(dado) {
	
	if (dado.classList){
		dado.classList.remove("is-invalid");
		dado.classList.remove("invalido");
		dado.classList.add("form-control");
		dado.classList.add("is-valid");
		dado.classList.add("valido");
	}else{
		dado.className += ' form-control is-valid';
	}
}

function ClassAddInvalid(dado) {

	if (dado.classList){
		dado.classList.remove("is-valid");
		dado.classList.remove("valido");
		dado.classList.add("form-control");
		dado.classList.add("is-invalid");
		dado.classList.add("invalido");
		
	}else{
		dado.className += ' form-control is-invalid';
	}
}

$("#submit_button").click( function Validador(event){

	let forms = document.getElementsByClassName('avalidar')[0];

	const dados = forms.getElementsByTagName('input');
	
	let JsonEviar = new FormData(forms);

	$.ajax({
		type: "POST",
		url: '/model/ajax/validar/login/',
		data: JsonEviar,
		success: function( data ) {
		
			if (data == '0') {

				ClassAddValid(dados[1])
				ClassAddValid(dados[2])

				if(forms.checkValidity()) {
				
					forms.submit();
				}
			} else if (data == '1') {
				ClassAddInvalid(dados[1])
			
			}else if (data == '2'){
				ClassAddInvalid(dados[2])
		
			}else if (data == '3'){

				ClassAddInvalid(dados[1])
				ClassAddInvalid(dados[2])
	
			}		
		},
		processData: false,
    	contentType: false
	});
});

$("#id_username").blur(function ValidarIncrevase(){

	let forms = document.getElementsByClassName('avalidar')[0];
	console.log(forms)
	const Input = document.getElementById(this.id)
	console.log(Input)
	let JsonEviar = new FormData(forms);

	$.ajax({
		type: "POST",
		url: '/model/ajax/validar/inscrevase/' + this.name,
		data: JsonEviar,
		success: function( data ) {
			console.log(data)
			if (data == '0') {

				ClassAddValid(Input)

				if(forms.checkValidity()) {
				
					forms.submit();
				}
			} else if (data == '1') {
				ClassAddInvalid(Input)
			}	
		},
		processData: false,
    	contentType: false
	});
});

$("#id_password").blur(function ValidarIncrevase(){

	let forms = document.getElementsByClassName('avalidar')[0];
	console.log(forms)
	const Input = document.getElementById(this.id)
	console.log(Input)
	let JsonEviar = new FormData(forms);

	$.ajax({
		type: "POST",
		url: '/model/ajax/validar/inscrevase/' + this.name,
		data: JsonEviar,
		success: function( data ) {
			console.log(data)
			if (data == '0') {

				ClassAddValid(Input)

				if(forms.checkValidity()) {
				
					forms.submit();
				}
			} else if (data == '1') {
				ClassAddInvalid(Input)
			}	
		},
		processData: false,
    	contentType: false
	});
});

