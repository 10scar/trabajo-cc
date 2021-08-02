
$(document).ready(function(){
	$(".pregunta-s").change(function(){
    valor = parseInt($('input[name=pregunta-ser-3]').val());
    valor2= parseInt($('input[name=pregunta-ser-1]').val());
    valor3 = parseInt($('input[name=pregunta-ser-2]').val());
    suma = valor +valor2+valor3;
    if(suma >10)
    {
      sobrante =  suma - (2*valor);
    if(sobrante >10)
      {

        restarvalue1 = 10 - valor3 - valor2;
        restarvalue2 = valor3;
        if(restarvalue1 < 0)
        {
          restarvalue1 = 10- valor - valor3;

        }
      }
      else
      {
        restarvalue2 = 10 - valor -valor2;
        restarvalue1 = 10 -restarvalue2 - valor;
        if(restarvalue2 <0)
        {
          restarvalue2 = 0;
          restarvalue1 = 10 - valor
        }
      }


      $('input[name=pregunta-ser-1]').val(restarvalue1);
      $('#p1').text(restarvalue1);

      $('input[name=pregunta-ser-2]').val(restarvalue2);
      $('#p2').text(restarvalue2);
      //alert(suma);

    }


	});

});
