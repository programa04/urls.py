let Valor = '500.00'
$("#Valor").val(Valor)
$.when( $.ready ).then(function() {

    let userLang = document.getElementsByTagName('html')[0].lang

    $.ajax({
        method: "GET",
        url: '/locale_teste/ajax/idioma/cpf/' + userLang,
        dataType: 'text',
        success: function(data) {

            for (let value of $('.documents')) {
                value.innerHTML = data
            }
        },
        processData: false,
        contentType: false
    });

});

$.when( $.ready ).then(function() {

    $.ajax({
        method: "GET",
        url: '/ajax/pmnt/id',
        dataType: 'json',
        success: function( data ) {
            PagSeguroDirectPayment.setSessionId(data.id);
        },
        complete: function() {MeiosPagamento();},
        processData: false,
        contentType: false
    });
});

$('#cardNumber').on('input',function MarcaPagamento() {
    console.log(this.value)
    let numeroCartao = this.value
    if (numeroCartao.length > 5) {
        PagSeguroDirectPayment.getBrand({
            cardBin: numeroCartao,
            success: function(response) {
                //console.log($('#BandeiraCartao')[0].innerHTML)
                let Nome = response.brand.name
                let imagem = "<img src='https://stc.pagseguro.uol.com.br/public/img/payment-methods-flags/68x30/" + Nome + ".png'>"
                //console.log(imagem)
                $('#BandeiraCartao')[0].innerHTML = imagem
                Parecelas(Nome)
                $('#Parcelas').removeClass('invisible')
            },
            error: function(response) {
                // Callback para chamadas que falharam.
                console.log(response)
                let alerta = "<div style='width: 18rem;' class='alert alert-dark alert-dismissible fade show' role='alert'> Cartão Invalido <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>"
                $('#BandeiraCartao')[0].innerHTML = alerta
            },
        });
    }else{
        $('#BandeiraCartao')[0].innerHTML = ''
        $('#Parcelas')[0].innerHTML = ''
        $('#Parcelas').addClass('invisible')
    }
})

function MeiosPagamento() {

    PagSeguroDirectPayment.getPaymentMethods({
        amount: Valor,
        success: function(response) {
            // Retorna os meios de pagamento disponíveis.
            // console.log('success')
            // console.log(response)
            $.each(response.paymentMethods.CREDIT_CARD.options, function(i, obj){
                //console.log(obj.images.MEDIUM.path)
                $('#CartaoCredito').append(
                    "<div class = 'mx-auto'><img src='https://stc.pagseguro.uol.com.br" + obj.images.MEDIUM.path+"' > " + obj.name +" </div>"
                )
            });
            $('#Boleto').append(
                "<div class = 'mx-auto'><img src='https://stc.pagseguro.uol.com.br" + response.paymentMethods.BOLETO.options.BOLETO.images.MEDIUM.path+"' > " + response.paymentMethods.BOLETO.name +" </div>"
            )
            $.each(response.paymentMethods.ONLINE_DEBIT.options, function(i, obj){
                //console.log(obj.images.MEDIUM.path)
                $('#CartaoDebito').append(
                    "<div class = 'mx-auto'><img src='https://stc.pagseguro.uol.com.br" + obj.images.MEDIUM.path+"' > " + obj.name +" </div>"
                )
            });
        },
        error: function(response) {
            // Callback para chamadas que falharam.
            //console.log('error')
            //console.log(response)
        },
        complete: function(response) {

        }
    });
}

function Parecelas (Bandeira){
    $("#brand").val(Bandeira)
    PagSeguroDirectPayment.getInstallments({
        amount: Valor,
        maxInstallmentNoInterest: 3,
        brand: Bandeira,
        success: function(response){
            //console.log(response)
            $.each(response.installments, function(i, obj){

                $('#Parcelas')[0].innerHTML = ''
                for (o of obj) {
                    //console.log(o)
                    let op = "<option value='" + o.quantity + " x "+ o.installmentAmount + "'>" + o.quantity + " x "+ o.installmentAmount + "</option>"
                    //console.log(op)
                    //console.log($('#Parcelas'))
                    $('#Parcelas')[0].innerHTML = $('#Parcelas')[0].innerHTML + op
                }

            });
       },
        error: function(response) {
            $('#Parcelas')[0].innerHTML = ''
       },
        complete: function(response){

       }
    });
}

function TokenCard() {
    PagSeguroDirectPayment.createCardToken({
        cardNumber: $("#cardNumber").val(), // Número do cartão de crédito
        brand: $("#brand").val(), // Bandeira do cartão
        cvv: $("#cvv").val(), // CVV do cartão
        expirationMonth: $("#expirationMonth").val(), // Mês da expiração do cartão
        expirationYear: $("#expirationYear").val(), // Ano da expiração do cartão, é necessário os 4 dígitos.
        success: function(response) {
            //console.log('Token')
            $("#TokenCard").val(response.card.token)
            //console.log(response.card.token)
        },
        error: function(response) {
            // Callback para chamadas que falharam.
        },
        complete: function(response) {
            // Callback para todas chamadas.
        }
    });
}

$('#ConfirmarPagamento').on( "click", function(event) {
    event.preventDefault();
    TokenCard();
    PagSeguroDirectPayment.onSenderHashReady(function(response){
        if(response.status == 'error') {
            //console.log(response.message)
            return false;
        }
        let hash = response.senderHash; //Hash estará disponível nesta variável.
        $("#HashCard").val(response.senderHash)

        //console.log($("#PagamentoForm"))
        $("#PagamentoForm").submit()
        //console.log(response)
    });
});
