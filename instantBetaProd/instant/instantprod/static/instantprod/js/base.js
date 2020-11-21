$.when( $.ready ).then(function() {

    let userLang = document.getElementsByTagName('html')[0].lang

    $.ajax({
        method: "GET",
        url: '/ajax/aprentacao/download/' + userLang,
        dataType: 'text',
        success: function( data ) {

            let Link_Download = document.getElementById('Download_Apresentacao')
            //console.log(Link_Download)
            //console.log('Funcionou')
            //console.log(data)
            Link_Download.href = data
            //console.log(Link_Download)
        },
        processData: false,
        contentType: false
    });

});


$("#botao_busca").change( function Busca(event){

    let dado = document.getElementById("botao_busca");
    console.log(dado.value)
    $.ajax({
        method: "GET",
        url: 'ajax/busca/' + dado.value,
        dataType: 'text',
        success: function( data ) {

            console.log(data)
            console.log('Funcionou')

        },
        processData: false,
        contentType: false
    });
});