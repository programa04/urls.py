
        $(".testeSelect").on("change", function () {
            let valor = $(this).val();
            alert(valor)
        });



        let modal = [document.getElementsByClassName('modal-body_2')[0].innerHTML]

        $(".adicionar_certifido").click(function () {
            $('.modal-body_2').append( '<br>' + modal);
            $(".remover_certificado").removeAttr('disabled');
        });

        $(".remover_certificado").click(function () {
            let remover = document.getElementsByClassName('teste-codigo')
            console.log(remover)
            remover[remover.length-1].innerHTML = ''
            console.log(remover)
        });



        //Adicionar campos de lingua e proeficiência
        var form_completo = document.getElementsByClassName("dede")[0].innerHTML;
        $(".add-campo").click(function () {
            $(".dede").append('<br>' + form_completo);
        });

        //Adicionar campos de lingua de partida e lingua de chegada
        var form_completo2 = document.getElementsByClassName("dede2")[0].innerHTML;
        $(".add-campo2").click(function () {
            $(".dede2").append('<br>' + form_completo2);
        });


        $(".checkbox_language").click(function () {
            let checkbox = document.getElementsByClassName('checkbox_language');
            for (let entrada of checkbox) {
                if (entrada.type == "checkbox" && entrada.checked) {
                    $('.button_save').removeAttr('disabled')
                }
            }
        })
