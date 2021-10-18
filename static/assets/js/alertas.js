import { NotyfEvent } from "../vendor/notyf/notyf.es";

document.getElementById('guardar_articulo').addEventListener('click', function (){
    const notyf = new NotyfEvent({
        position: {
            x: 'center',
            y: 'top',
        },
        types: [
            {
                type: 'info',
                background: 'gren',
                icon: {
                    className: 'fas fa-info-circle',
                    tagName: 'span',
                    color: '#fff'
                },
                dismissible: false
            }
        ]
    });
    notyf.open({
        type: 'success',
        message: 'Guardado correctamente !'
    });
});

document.getElementById('hablar').addEventListener('click', function (){
    const notyf = new NotyfEvent({
        position: {
            x: 'center',
            y: 'top',
        },
        types: [
            {
                type: 'success',
                background: 'gren',
                icon: {
                    className: 'fas fa-info-circle',
                    tagName: 'span',
                    color: '#fff'
                },
                dismissible: false
            }
        ]
    });
    notyf.open({
        type: 'info',
        message: 'Habla tu artículo'
    });
});
