//$.when( $.ready ).then(function() {

//	let userLang = document.getElementsByTagName('html')[0].lang

//	$.ajax({
//		method: "GET",
//		url: '/ajax/idioma/cpf/' + userLang,
//		dataType: 'text',
//		success: function(data) {
            
//			let Select = document.getElementById('documents')
//			Select.innerHTML = data
//		},
//		processData: false,
//		contentType: false
//	});

//});

$("#registration_form_submit").click( function(){

    let form_data = $("#form_reg").serializeArray()
    let data = {}

    form_data.forEach(function (element, index, array){
        data[element.name] = element.value
    });
    //delete data.csrfmiddlewaretoken
    console.log(data)

    $.ajax({
        method: "POST",
        url: '/instantAPI/users/',
        dataType: 'json',
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
        },
        data: JSON.stringify(data),
        success: function( data ) {
            console.log(data)
            console.log('Funcionou')
        },
        processData: false,
        contentType: 'application/json'
    });
});