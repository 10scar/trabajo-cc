$(document).ready(function(){
	$(".pregunta-alt").change(function(){
    valor = parseInt($('input[name=pregunta-alt-1]').val());
    valor2= parseInt($('input[name=pregunta-alt-2]').val());
    suma = valor +valor2;
    if(suma >10)
    {
      restarvalue1 =  10 - valor2;
      restarvalue2 = valor2;


      $('input[name=pregunta-alt-1]').val(restarvalue1);
      $('#altp1').text(restarvalue1);

      $('input[name=pregunta-alt-2]').val(restarvalue2);
      $('#altp2').text(restarvalue2);
      //alert(suma);

    }


	});

});
