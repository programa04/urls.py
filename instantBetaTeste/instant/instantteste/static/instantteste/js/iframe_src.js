var link_id

function Sumir(id){
    link_id = id;
};

function AtributosFrame(){

    var x = document.getElementById("I1");
    var y = (x.contentWindow || x.contentDocument);
    if (y.document)y = y.document;
    var j = y.getElementsByTagName("strong");
    var a = document.getElementsByClassName("count");
    if (a[0] == undefined) {
        var pg = document.getElementById("ProgessBar");
        pg.style.width = "100%";
        pg.innerHTML = "100%";
        $( "#Form_2" ).submit();
    } else {
        if (j[0] != undefined) {
            if (j[0].innerHTML == "Relatorio Salvo") {
                window.scrollTo(10, 300);
                var q = 100 / a.length;
                var xl = a.length;
                var z = parseInt(document.getElementById("ProgessBar").attributes[3].value);
                var h = z+q;
                var k = h.toFixed(0);
                var c = k/q.toFixed(0);
        
                if (k<100) {
                    if (c.toFixed(0)==xl) {
                        var pg = document.getElementById("ProgessBar");
                        pg.style.width = "100%";
                        pg.innerHTML = "100%";
                        link_id.style.display = "none";
                        $( "#Form_2" ).submit();
                    }else {
                        var pg = document.getElementById("ProgessBar");
                        pg.attributes[3].value = k.toString();
                        pg.style.width = k.toString()+"%";
                        pg.innerHTML = k.toString()+"%";
                        link_id.style.display = "none";
                        
                    }
                } else if (k==100) {
                    var pg = document.getElementById("ProgessBar");
                    pg.style.width = "100%";
                    pg.innerHTML = "100%";
                    link_id.style.display = "none";
                    $( "#Form_2" ).submit();
                } else {
                    var pg = document.getElementById("ProgessBar");
                    pg.style.width = "100%";
                    pg.innerHTML = "100%";
                    link_id.style.display = "none";
                    $( "#Form_2" ).submit();
                }	
            } else {
                window.scrollTo(10, 300);
            }
        }    
    }
}
