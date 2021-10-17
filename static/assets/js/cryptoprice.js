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