from flask import Flask

app = Flask(__name__)

# ANA SAYFA
@app.route('/')
def ana_sayfa():
    return """
    <html>
    <head>
        <title>Erkan'ın Sitesi</title>
        <style>
            body { margin: 0; padding: 0; text-align: center; font-family: 'Arial', sans-serif;
                   background-image: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb');
                   background-size: cover; background-position: center; background-attachment: fixed;
                   color: white; height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; }
            h1 { font-size: 40px; text-shadow: 2px 2px 5px black; }
            .oyun-kutusu {
                display: flex; flex-direction: column; align-items: center; justify-content: center;
                width: 150px; height: 150px; background: rgba(255, 255, 255, 0.2); 
                border-radius: 20px; text-decoration: none; color: white; margin-top: 30px;
                backdrop-filter: blur(10px); border: 2px solid white;
            }
        </style>
    </head>
    <body>
        <h1>Erkan'ın Web Sitesine Hoş Geldiniz!</h1>
        <a href="/oyunlar" class="oyun-kutusu">
            <img src="https://cdn-icons-png.flaticon.com/512/3202/3202926.png" style="width: 60px; margin-bottom: 10px;">
            <span style="font-size: 20px; font-weight: bold;">Oyunlar</span>
        </a>
    </body>
    </html>
    """

# OYUNLAR MENÜSÜ
@app.route('/oyunlar')
def oyunlar():
    return """
    <html>
    <body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <h1>Oyun Seçiniz</h1>
        <div style="margin-top:50px;">
            <a href="/xox-oyunu" style="color:yellow; font-size:30px; text-decoration:none;">Tic Tac Toe (XOX)</a>
        </div>
        <br><br>
        <a href='/' style='color:white; text-decoration:none;'>Geri Dön</a>
    </body>
    </html>
    """

# XOX OYUNU
@app.route('/xox-oyunu')
def xox_oyunu():
    return """
    <html>
    <head><title>Tic Tac Toe</title></head>
    <body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <h1>Tic Tac Toe</h1>
        <div id="board" style="display:grid; grid-template-columns:repeat(3, 100px); gap:10px; justify-content:center;">
            <div onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
        </div>
        <script>let t='X'; function p(c){if(!c.innerText){c.innerText=t; t=t==='X'?'O':'X';}}</script>
        <br><br><a href='/oyunlar' style='color:yellow; text-decoration:none;'>Oyunlar Menüsüne Dön</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
