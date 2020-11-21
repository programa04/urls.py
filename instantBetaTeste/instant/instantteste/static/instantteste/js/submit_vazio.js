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
			
			$.get('ajax/vazio/', function(resultado){
				let Html = document.getElementById('alerta')
				console.log(Html.innerHTML)
				Html.innerHTML = resultado + Html.innerHTML
				return true
			});	
			
		} else {
			$( "#Form" ).submit();
		}	
	});
});
