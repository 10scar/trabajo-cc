

$(document).ready(function(){
	$(".pregunta-m").change(function(){
    valor = parseInt($('input[name=pregunta-mundo-3]').val());
    valor2= parseInt($('input[name=pregunta-mundo-1]').val());
    valor3 = parseInt($('input[name=pregunta-mundo-2]').val());
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


      $('input[name=pregunta-mundo-1]').val(restarvalue1);
      $('#mp1').text(restarvalue1);

      $('input[name=pregunta-mundo-2]').val(restarvalue2);
      $('#mp2').text(restarvalue2);
      //alert(suma);

    }


	});

});
