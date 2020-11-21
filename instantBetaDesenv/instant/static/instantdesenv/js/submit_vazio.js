$(document).ready(function procura(){
	$( ".bt" ).click(function() {
		var valor = $( "input:checked" ).each(function() {
			var vari = $( this ).val();
			console.log(vari);
			const newLocal = "valor";
			console.log(newLocal);
		}).get();
		console.log(valor);
		if (valor[0] == undefined) {
			alert( "Escolha uma Opção" );
		} else {
			$( "#Form" ).submit();
		}	
	});
});
