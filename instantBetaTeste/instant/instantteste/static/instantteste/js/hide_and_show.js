$(document).ready(function(){
	$(".r1").click(function(){
		$("#R2").hide();
		$("#R3").hide();
		$("#R4").hide();
		$("#R5").hide();
		$("#R6").hide();
		$("#R7").hide();
		$("#R8").hide();
		$("#R1").show();
	});
});
$(document).ready(function(){
	$(".r2").click(function(){
		$("#R1").hide();
		$("#R3").hide();
		$("#R4").hide();
		$("#R5").hide();
		$("#R6").hide();
		$("#R7").hide();
		$("#R8").hide();
		$("#R2").show();
	});
});
$(document).ready(function(){
	$(".r3").click(function(){
		$("#R1").hide();
		$("#R2").hide();
		$("#R4").hide();
		$("#R5").hide();
		$("#R6").hide();
		$("#R7").hide();
		$("#R8").hide();
		$("#R3").show();
	});
});
$(document).ready(function(){
	$(".r4").click(function(){
		$("#R1").hide();
		$("#R2").hide();
		$("#R3").hide();
		$("#R5").hide();
		$("#R6").hide();
		$("#R7").hide();
		$("#R8").hide();
		$("#R4").show();
	});
});
$(document).ready(function(){
	$(".r5").click(function(){
		$("#R1").hide();
		$("#R2").hide();
		$("#R3").hide();
		$("#R4").hide();
		$("#R6").hide();
		$("#R7").hide();
		$("#R8").hide();
		$("#R5").show();
	});
});
$(document).ready(function(){
	$(".r6").click(function(){
		$("#R1").hide();
		$("#R2").hide();
		$("#R3").hide();
		$("#R4").hide();
		$("#R5").hide();
		$("#R7").hide();
		$("#R8").hide();
		$("#R6").show();
	});
});
$(document).ready(function(){
	$(".r7").click(function(){
		$("#R1").hide();
		$("#R2").hide();
		$("#R3").hide();
		$("#R4").hide();
		$("#R5").hide();
		$("#R6").hide();
		$("#R8").hide();
		$("#R7").show();
	});
});
$(document).ready(function(){
	$(".r8").click(function(){
		$("#R1").hide();
		$("#R2").hide();
		$("#R3").hide();
		$("#R4").hide();
		$("#R5").hide();
		$("#R6").hide();
		$("#R7").hide();
		$("#R8").show();
	});
});

function desmarcar(){
	var ck1 = document.getElementById("id_Planos_0")
	var ck2 = document.getElementById("id_Franqueamento_0")
	var ck3 = document.getElementById("id_Franqueamento_1")
	var ck4 = document.getElementById("id_Franqueamento_2")
	var ck5 = document.getElementById("id_Oportunidades_0")
	var ck6 = document.getElementById("id_Oportunidades_1")
	if (ck1.checked == true) {
		ck2.checked = false;
		ck3.checked = false;
		ck4.checked = false;
		ck5.checked = false;
		ck6.checked = false;
	} else if 
		(
			ck2.checked == true || 
			ck3.checked == true || 
			ck4.checked == true
		) 
	{
		ck1.checked = false;
		ck5.checked = false;
		ck6.checked = false;
	
	} else if 
		(
			ck5.checked == true || 
			ck6.checked == true
		) 
	{
		ck1.checked = false;
		ck2.checked = false;
		ck3.checked = false;
		ck4.checked = false;
	}
}
