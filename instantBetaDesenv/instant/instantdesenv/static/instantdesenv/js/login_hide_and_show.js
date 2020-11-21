$(document).ready(function(){
  $("#troca").click(function(){
    $(".Cadastro").hide();
    $("#troca").hide();
    $("#LogShow").show();
    $("#volta").show();
  });
});

$(document).ready(function(){
  $("#volta").click(function(){
    $("#LogShow").hide();
    $("#volta").hide();
    $(".Cadastro").show();
    $("#troca").show();
  });
});