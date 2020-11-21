function AtributosFrame(){

    var x = document.getElementById("I1");
    var y = (x.contentWindow || x.contentDocument);
    if (y.document)y = y.document;
    var j = y.getElementsByTagName("strong");
    if (j[0] != undefined) {
        if (j[0].innerHTML == "Relatorio Salvo") {
            window.scrollTo(10, 10);
            var a = document.getElementsByClassName("count");
            var q = 100 / a.length;
            var xl = a.length;
            var z = parseInt(document.getElementById("ProgessBar").attributes[3].value);
            var h = z+q;
            var k = h.toFixed(0);
            var c = k/q.toFixed(0);
    
            if (k<100) {
                if (c.toFixed(0)==xl) {
                    document.getElementById("ProgessBar").style.width = "100%";
                    var bt = document.getElementsByClassName("Aparecer");
                    bt[0].style.visibility = "visible";
                }else {
                    document.getElementById("ProgessBar").attributes[3].value = k.toString();
                    document.getElementById("ProgessBar").style.width = k.toString()+"%";
                }
            } else if (k==100) {
                document.getElementById("ProgessBar").attributes[3].value = k.toString();
                document.getElementById("ProgessBar").style.width = k.toString()+"%";
                var bt = document.getElementsByClassName("Aparecer");
                bt[0].style.visibility = "visible";
            } else {
                document.getElementById("ProgessBar").style.width = "100%";
                var bt = document.getElementsByClassName("Aparecer");
                bt[0].style.visibility = "visible";
            }	
        } else {
            window.scrollTo(10, 10);
        }
    }    
}
