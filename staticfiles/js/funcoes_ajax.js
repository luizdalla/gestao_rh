// function teste(){
//     alert("Funcionou!!!");
// }




function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    valor = document.getElementById("campox").value;
    console.log(valor);

    $.ajax({
        type: 'POST',
        url: '/horaextra/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
            outro_parametro: valor,
        },
        success: function(result){
            console.log("Sucesso");
            console.log(result);
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}
function naoUtilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horaextra/nao-utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log("Sucesso");
            console.log(result);
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}