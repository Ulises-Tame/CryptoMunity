from flask_login import current_user



def check_user():
    if current_user.tipoUsuario == 'Trader':
        return True
    else:
        return None

def check_sentimiento(sentimiento):
    if sentimiento == 'positive':
        valoración = 5
    elif sentimiento == 'neutral':
        valoración = 2.5
    elif sentimiento == 'negative':
        valoración = 0
 
    return valoración