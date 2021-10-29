from flask_login import current_user
from include.DAO import get_boton


def check_user():
    if current_user.tipoUsuario == 'Trader':
        return True
    else:
        return None

def check_sentimiento(sentimiento):
    if sentimiento == 'positive':
        valoración = 5
    elif sentimiento == 'neutral' or sentimiento == 'mixed':
        valoración = 2.5
    elif sentimiento == 'negative':
        valoración = 1
    
    return valoración

def promedio(valores):
    contador = 0
    lista=[]
    for valor in valores:
        sentimiento = valor.sentimiento
        lista.append(sentimiento)
        print(sentimiento)
        contador = sentimiento + contador    
    narticulos = lista.__len__()
    #if contador == 0 or narticulos == 0 or contador == None or narticulos == None:
    #   resultado = 0
    #else:
    #print(contador)
    resultado = int(contador / narticulos)
    #print(resultado)
    
    if resultado >= 3:
        tipo = "success"
    elif resultado < 3 and resultado >=2:
        tipo ="warning"
    elif resultado < 2:
        tipo ="danger"
    #print(tipo)
    boton = get_boton(tipo)
    return boton


 

    


