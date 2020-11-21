function RetornaContrato(id){
	// console.log(id.name)
	// console.log(id.name)
	// console.log(id.getElementsByTagName("input")[0])
	let InputId = id.getElementsByTagName("input")[0]
	$.get(InputId.name, function(resultado){
		// console.log(resultado)
		// console.log(Link)
		let DivId = document.getElementById("VerDocumento");
		// console.log(DivId)
		DivId.innerHTML = resultado;
	});
};

//  desabilitar o botão de download no caso de nenhuma opção estar marcada.

function RetornaParte(){
	let contratante = document.getElementById("id_Contratante");
	let contratado = document.getElementById("id_Contratado");
	let DivId = document.getElementById("lista_download");
	let lista = DivId.getElementsByTagName("input");
	
	$.get('ajax/parte/' + contratante.value, function(resultado){
		
		for (let index = 0; index < lista.length; index++) {
			const element = lista[index];
			let ids = element.value;
			let link = ids.replace("Contratante", resultado);
			element.value = link
			// console.log(link)
			
		}
		
	});
	$.get('ajax/parte/' + contratado.value, function(resultado){
		if (resultado == '0' || resultado == 'Contratante Invalido') {
			window.alert("Contratante não Existente. Tente Novamente")
		} else if (resultado == '0' || resultado == 'Contratado Invalido') {
			window.alert("Contratado não Existente. Tente Novamente")
		} else {
			for (let index = 0; index < lista.length; index++) {
				const element = lista[index];
				let ids = element.value;
				let link = ids.replace("Contratado", resultado);
				element.value = link
				// console.log(link)
			
			}
		}
		
	});	
};

$('#download_button').click(function DownloadDocumento(){
	// console.log(id.name)
	// console.log(id.name)
	// console.log(id.getElementsByTagName("input")[0])
	let Lista = document.getElementsByClassName("RetornaContrato");
	let frames = window.frames;
	let pagina = document.getElementById('Iframe');
	
	for (let index = 0; index <  Lista.length; index++) {
		const element =  Lista[index];
		let Input = element.getElementsByTagName("input")[0];
		//  checar o valor do input
		// console.log(Input.checked)
	
		if (Input.checked === true) {
			// console.log(pagina.innerHTML)
			pagina.innerHTML = pagina.innerHTML + '<iframe class = "invisible" src="" frameborder="0"></iframe>';
			setTimeout(function(){ 
				frames[index].location = 'documento/download/' + Input.value;
			}, 500*(index + 1));
			// console.log('Aqui teste de tempo ', index)
			// $.get('documento/download/' + Input.value, function(resultado){
			// 	return resultado
			// });
		}	
	}
});

$(document).ready(function EnviaForm(){
	$( ".Enviar" ).click(function() {
		// console.log('foi algo');
		$( "#Form" ).submit();
	});
});

$("#id_LinguaClausula").change(function Lingua(){
	// console.log('foi algo')
	
	let Valor = document.getElementById("id_LinguaClausula").value;
	let Seletor = document.getElementById("id_Pais")
	// console.log(Valor)
	if (!Valor){
		// console.log('undefined')
		let link = 'ajax/lingua' + '/' + null
		$.get(link, function(resultado){
			// console.log(resultado)
			// console.log(link)
			Seletor.innerHTML = resultado;
		});	
	} else {
		let link = 'ajax/lingua' + '/' + Valor
		$.get(link, function(resultado){
			// console.log(resultado)
			// console.log(link)
			Seletor.innerHTML = resultado;
		});		
	}
});

$("#id_Pais").change(function Pais(){
	// console.log('foi algo')
	
	let Valor = document.getElementById("id_Pais").value;
	let Seletor = document.getElementById("id_LinguaClausula")
	// console.log(Valor)
	if (!Valor){
		// console.log('undefined')
		let link = 'ajax/pais' + '/' + null
		$.get(link, function(resultado){
			// console.log(resultado)
			// console.log(link)
			// console.log(Seletor.innerHTML)
			Seletor.innerHTML = resultado;
		});
	} else {
		let link = 'ajax/pais' + '/' + Valor
		$.get(link, function(resultado){
			// console.log(resultado)
			// console.log(link)
			// console.log(Seletor.innerHTML)
			Seletor.innerHTML = resultado;
		});		
	}

});

