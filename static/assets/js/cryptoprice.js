let ws = new WebSocket('wss://stream.binance.com:9443/ws/ethusdt@trade');
let cryptoPrice = document.getElementById('crypto-price');

ws.onmessage = (event) => {
    let crypto = JSON.parse(event.data);
    cryptoPrice.innerText ='$'+parseFloat(crypto.p) 
}


let wsbtc = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@trade');
let cryptoPriceBTC = document.getElementById('btc-price');

wsbtc.onmessage = (event) => {
    let cryptoBtc = JSON.parse(event.data);
    cryptoPriceBTC.innerText ='$'+parseFloat(cryptoBtc.p) 
}


let wssol = new WebSocket('wss://stream.binance.com:9443/ws/solusdt@trade');
let cryptoPriceSol = document.getElementById('sol-price');

wssol.onmessage = (event) => {
    let cryptoSol = JSON.parse(event.data);
    console.log(event.data)
    cryptoPriceSol.innerText ='$'+parseFloat(cryptoSol.p) 
}


let wsdoge = new WebSocket('wss://stream.binance.com:9443/ws/dogeusdt@trade');
let cryptoPriceDoge = document.getElementById('doge-price');

wsdoge.onmessage = (event) => {
    let cryptoDoge = JSON.parse(event.data);
    console.log(event.data)
    cryptoPriceDoge.innerText ='$'+parseFloat(cryptoDoge.p) 
}


let wscake = new WebSocket('wss://stream.binance.com:9443/ws/cakeusdt@trade');
let cryptoPriceCake = document.getElementById('cake-price');

wscake.onmessage = (event) => {
    let cryptoCake = JSON.parse(event.data);
    console.log(event.data)
    cryptoPriceCake.innerText ='$'+parseFloat(cryptoCake.p) 
}


let wsada = new WebSocket('wss://stream.binance.com:9443/ws/adausdt@trade');
let cryptoPriceAda = document.getElementById('ada-price');

wsada.onmessage = (event) => {
    let cryptoAda = JSON.parse(event.data);
    console.log(event.data)
    cryptoPriceAda.innerText ='$'+parseFloat(cryptoAda.p) 
}