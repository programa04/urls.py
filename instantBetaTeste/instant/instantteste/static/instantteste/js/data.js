$( function() {
  $( "#id_first_name" ).datepicker({
		format: "dd/mm/yyyy",
		todayBtn: "linked",
		clearBtn: true,
		language: "pt-BR",
		todayHighlight: true
	});
});

$( function() {
  $( ".DataIn" ).datepicker({
		format: "dd/mm/yyyy",
		todayBtn: "linked",
		clearBtn: true,
		language: "pt-BR",
		todayHighlight: true,
		startDate: "today"
	});
});

$( function() {
	$( ".AniIn" ).datepicker({
		format: "dd/mm/yyyy",
		todayBtn: "linked",
		clearBtn: true,
		language: "pt-BR",
		todayHighlight: true
	});
});