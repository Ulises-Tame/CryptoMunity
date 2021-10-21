const hablar = document.getElementById('hablar');
    hablar.addEventListener('click', function () {
        $.ajax({
            url: "/voz",
            type: "POST",
            dataType: 'json',
            data:{'texto': response},
            success: function(){
                
            
            },
            error: function(){
            // Se ejecuta cuando es imposible obtener
            // los datos de la url
            },
            async: false, // La petición es síncrona
            cache: false // No queremos usar la caché del navegador
            });
           
        });

