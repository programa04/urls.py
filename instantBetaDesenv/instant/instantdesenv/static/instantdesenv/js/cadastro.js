$.when( $.ready ).then(function() {

    let userLang = document.getElementsByTagName('html')[0].lang

    $.ajax({
        method: "GET",
        url: '/ajax/idioma/cadastro/' + userLang,
        dataType: 'text',
        success: function( data ) {
            
            let Inputs = document.getElementsByClassName('IdiomaCadastro')
            let campos = data.split("///")
            
            //console.log('Funcionou')
            //console.log(data)

            let i = 0;
            for (let Input of Inputs) {

                Input.placeholder = campos[i]
                i++;
            }

        },
        processData: false,
        contentType: false
    });
    
});

$.when( $.ready ).then(function() {

    let userLang = document.getElementsByTagName('html')[0].lang

    $.ajax({
        method: "GET",
        url: '/ajax/idioma/cpf/' + userLang,
        dataType: 'text',
        success: function(data) {
            
            let Select = document.getElementById('documents')
            Select.innerHTML = data
        },
        processData: false,
        contentType: false
    });

});

$("#documents").click(function() {

    let userLang = document.getElementsByTagName('html')[0].lang
    let info = document.getElementById('caixa_info')

    if (!info) {
        
        $.ajax({
            method: "GET",
            url: '/ajax/idioma/' + userLang,
            dataType: 'text',
            success: function( data ) {

                $("#id_alerta").after(data);
                //$("#id_alerta").attr( "title", data);
                console.log('Funcionou')

            },
            processData: false,
            contentType: false
        });

    } 

});

$(".country_code").click(function() {
    //console.log('teste')
    let selecionado = document.getElementById('dropdownMenu2')
    let input_label = this.getElementsByClassName('label_codigo')[0]
    let info = document.getElementById('caixa_info')
    //console.log(this)
    //console.log(selecionado.innerHTML)
    //console.log(input_label.innerHTML)
    selecionado.innerHTML = input_label.innerHTML
});

$(".termo").click(function() {

    let botao = document.getElementById('submit_button_join')
    
    if (
            $("#Termo:checked").length == 0 
            || $("#Termo16:checked").length == 0
            || $("#Termo_offers:checked").length == 0
            || $("#Termo_newsletter:checked").length == 0
            || $("#Termo_notifica:checked").length == 0
        ) {
        $("#submit_button_join").attr("disabled","disabled");
        console.log($("#Termo:checked").length)
        console.log('false')

    } else if (
        $("#Termo:checked").length == 1 
            && $("#Termo16:checked").length == 1
            && $("#Termo_offers:checked").length == 1
            && $("#Termo_newsletter:checked").length == 1
            && $("#Termo_notifica:checked").length == 1
        ) {
        $("#submit_button_join").removeAttr("disabled");
        console.log($("#Termo:checked").length)
        console.log('true')

    } 

});
