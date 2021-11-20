# main.py
from flask import Blueprint, render_template, request, json, redirect, url_for, jsonify
from flask_login import login_required, current_user
from include.models import Articulos
from run import db
from include.DAO import ( 
get_all_articulos, 
get_all_photos, 
get_articulos_user_by_id, 
get_photo_by_id, 
update_articulo, 
get_articulo_by_id, 
get_articulos_by_crypto,
insert_articulo,
get_crypto,
getCryptoByName,
get_all_cryptos,
) 
from include.DAO_EVENTOS import (insert_evento_login, 
insert_evento_articulo, 
insert_evento_editararticulo, 
insert_evento_nuevoarticulo,
insert_vista_editararticulo,
insert_evento_crypto,
insert_evento_perfil,
insert_evento_cryptos
) 
from sentiment import sentiment_analysis, get_authenticate_client
from include.command import check_sentimiento, check_user, promedio
import json
from voz import from_mic as voz_funct

main = Blueprint('main', __name__, url_prefix= '')


@main.route('/')
def index():
    return render_template('accounts/landingpage.html')


@main.route('/cryptomunitylan')
def landing():
    return render_template('accounts/landingpage.html', segment='profile')

@main.route('/api', methods=["GET"])
def apiConsulta():
    nombreCrypto = request.args.get("cripto")
    crypto = getCryptoByName(nombreCrypto)
    print(crypto.descripcion)
    diccionario = {"descripcion": crypto.descripcion,
                    "link": crypto.link,
    }
    return jsonify(diccionario)

@main.route('/profile')
@login_required
def profile():
    if current_user.tipoUsuario == 'Trader':
        insert_evento_perfil()
        cryptos= get_all_cryptos()
        btc = get_articulos_by_crypto("BTC")
        eth = get_articulos_by_crypto("ETH")
        sol = get_articulos_by_crypto("SOL")
        doge = get_articulos_by_crypto("DOGE")
        cake = get_articulos_by_crypto("CAKE")
        cardano = get_articulos_by_crypto("ADA")

        botonBtc = promedio(btc)
        botonEth = promedio(eth)    
        botonSol = promedio(sol)
        botonDoge = promedio(doge)
        botonCake = promedio(cake)
        botonCardano = promedio(cardano)
        claseBtc = botonBtc.clase
        rankBtc = botonBtc.rank
        claseEth = botonEth.clase
        rankEth = botonEth.rank
        claseSol = botonSol.clase
        rankSol = botonSol.rank
        claseDoge = botonDoge.clase
        rankDoge = botonDoge.rank
        claseCake = botonCake.clase
        rankCake = botonCake.rank
        claseAda = botonCardano.clase
        rankAda = botonCardano.rank

        return render_template('accounts/profile_trader.html', name=current_user.nombreUsuario, segment='profile', claseBtc = claseBtc, rankBtc = rankBtc, claseEth = claseEth, rankEth = rankEth, claseSol = claseSol, rankSol = rankSol, claseDoge = claseDoge, rankDoge = rankDoge, claseCake = claseCake, rankCake = rankCake, claseAda = claseAda, rankAda = rankAda, cryptos=cryptos )
    else:
        insert_evento_perfil()
        return redirect(url_for('main.profile_investigador'))

@main.route('/cryptos')
@login_required
def cryptomonedas():
    if current_user.tipoUsuario == 'Trader':
        cryptos= get_all_cryptos()
        insert_evento_cryptos()
        return render_template('accounts/cryptos.html', name=current_user.nombreUsuario, segment='profile', cryptos = cryptos)
    else:
        return redirect(url_for('main.profile_investigador'))        

@main.route('/art-trader/<string:crypto>')
@login_required
def articulos_trader(crypto):
    user = check_user()
    if  user:
        pass
    else: 
        return redirect(url_for('main.profile'))  
    articulos = get_articulos_by_crypto(crypto)
    boton = promedio(articulos)
    criptomoneda = get_crypto(crypto)
    for crypto_ in criptomoneda:
        nombrecrypto = crypto_.nombreCriptomoneda
        foto = crypto_.fotoCrypto
        descripcion = crypto_.descripcion
    clase = boton.clase
    rank = boton.rank
    insert_evento_crypto()
    return render_template('accounts/trader_articulos.html', name=current_user.nombreUsuario, segment='profile', articulos_crypto=articulos, nombrecrypto=nombrecrypto, fotocrypto=foto, descripcion=descripcion, clase=clase, rank=rank)

@main.route('/profile_investigador')
@login_required
def profile_investigador():
    user = check_user()
    if user:
        return redirect(url_for('main.profile'))
    articulos_user = get_articulos_user_by_id(current_user.id)
    #for articulos in articulos_user:
        #print(articulos.fechaDePublicacion)
    return render_template('accounts/profile_invest.html', nombre=current_user.nombreUsuario, segment='profile', articulos_user=articulos_user)

@main.route('/articulos')
@login_required
def articulos():
    user = check_user()
    if user:
        return redirect(url_for('main.profile'))
    fotos = get_all_photos()
    insert_evento_articulo()
    return render_template('accounts/agregar_articulo.html', nombre=current_user.nombreUsuario, segment='articulos', fotos=fotos)



@main.route('/articuloscrypto/<int:id>')
def leerArticulos(id):
    user = check_user()
    if  user:
        pass
    else: 
        return redirect(url_for('main.profile'))
    articulo = get_articulo_by_id(id)
    return render_template('accounts/leerarticulos.html', segment='articulos', articulo=articulo)



@main.route('/articulos', methods=['POST'])
@login_required
def articulos_post():
    user = check_user()
    if user:
        return redirect(url_for('main.profile'))
    publicación = request.form['publicación']
    titulo = request.form['titulo']
    crypto = request.form['crypto']
    imagen = request.form['img']
    cliente = get_authenticate_client()
    sentimiento = sentiment_analysis(cliente,publicación)
    valoración =  check_sentimiento(sentimiento)


    nuevo_articulo= Articulos(nombreArticulo=titulo, autorArticulo=current_user.nombreUsuario,articulo=publicación,noEdicion=1,estatusArticulo=1,cryptoRelacionada=crypto,idUsuario=current_user.id,sentimiento= valoración,fotoArticulo=str(imagen))
    insert_articulo(nuevo_articulo)
    insert_evento_nuevoarticulo()
    return redirect(url_for('main.profile'))


@main.route('/articulos/edit/<int:id>')
@login_required
def articulos_edit(id):
    user = check_user()
    if user:
        return redirect(url_for('main.profile'))
    articulo = get_articulo_by_id(id)
    print(articulo.cryptoRelacionada)
    insert_vista_editararticulo
    return render_template('accounts/editar.html', segment='articulos', articulo=articulo)

@main.route('/articulos/edit/<int:id>', methods=['POST'])
@login_required
def articulos_edit_post(id):
    user = check_user()
    if user:
        return redirect(url_for('main.profile'))
    publicación = request.form['publicación']
    titulo = request.form['titulo']
    cliente = get_authenticate_client()
    sentimiento = sentiment_analysis(cliente,publicación)
    valoración =  check_sentimiento(sentimiento)
    update_articulo(id,titulo,publicación,valoración)
    insert_evento_editararticulo()
    return redirect(url_for('main.profile'))

@main.route('/voz', methods=['POST'])
@login_required
def voz():
    texto = voz_funct()
    texto_json = {
        "speech": texto
    }
    print(texto)
    return jsonify(texto_json)
