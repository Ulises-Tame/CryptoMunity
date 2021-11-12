var hablar = document.getElementById('hablar');
var texto = "";
hablar.addEventListener('click', function () {
    $.ajax({
        url: "/voz",
        type: "POST",
        headers: {"Content-Type":"aplication/json"},
        dataType: 'json',
        data:JSON.stringify(texto),
        success: function(data){
            console.log(data);
             document.getElementById("txtvoz").textContent = data["speech"];
        }
        });
    });