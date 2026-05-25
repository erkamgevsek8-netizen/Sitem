from flask import Flask

app = Flask(__name__)

# ANA SAYFA ve OYUNLAR MENÜSÜ aynı kalıyor, sadece XOX'u güncelliyoruz...

@app.route('/')
def ana_sayfa():
    return """
    <html><head><title>Erkan'ın Sitesi</title></head>
    <body style="margin:0; background-image:url('https://images.unsplash.com/photo-1506744038136-46273834b3fb'); background-size:cover; text-align:center; color:white; height:100vh; display:flex; flex-direction:column; align-items:center; justify-content:center; font-family:Arial;">
        <h1>Erkan'ın Web Sitesine Hoş Geldiniz!</h1>
        <a href="/oyunlar" style="text-decoration:none; color:white; display:flex; flex-direction:column; align-items:center; background:rgba(255,255,255,0.2); padding:20px; border-radius:20px; border:2px solid white; backdrop-filter:blur(10px);">
            <img src="https://cdn-icons-png.flaticon.com/512/3202/3202926.png" style="width:60px; margin-bottom:10px;">
            <span style="font-size:20px; font-weight:bold;">Oyunlar</span>
        </a>
    </body></html>
    """

@app.route('/oyunlar')
def oyunlar():
    return """
    <body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <h1>Oyun Seçiniz</h1>
        <a href="/xox-oyunu" style="color:yellow; font-size:30px;">Tic Tac Toe (XOX)</a><br><br>
        <a href='/' style='color:white;'>Geri Dön</a>
    </body>
    """

@app.route('/xox-oyunu')
def xox_oyunu():
    return """
    <html>
    <body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <h1>Tic Tac Toe</h1>
        <button onclick="toggleMusic()" style="padding:10px; cursor:pointer;">🔊 Müzik Aç/Kapat</button>
        <audio id="bgMusic" loop src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"></audio>
        
        <div id="board" style="display:grid; grid-template-columns:repeat(3, 100px); gap:10px; justify-content:center; margin-top:20px;">
            <div class="cell" onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="cell" onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="cell" onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="cell" onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="cell" onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="cell" onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="cell" onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="cell" onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="cell" onclick="p(this)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
        </div>
        <h2 id="msg">Sıra X'te</h2>
        <script>
            let t='X', game=true;
            function toggleMusic(){ let m=document.getElementById('bgMusic'); m.paused ? m.play() : m.pause(); }
            function p(c){
                if(!c.innerText && game){
                    c.innerText=t;
                    check();
                    t=t==='X'?'O':'X';
                    if(game) document.getElementById('msg').innerText = "Sıra "+t+"'te";
                }
            }
            function check(){
                let cells = document.querySelectorAll('.cell');
                let wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
                for(let w of wins){
                    if(cells[w[0]].innerText && cells[w[0]].innerText===cells[w[1]].innerText && cells[w[1]].innerText===cells[w[2]].innerText){
                        document.getElementById('msg').innerText = cells[w[0]].innerText + " Kazandı!";
                        game=false; return;
                    }
                }
                if([...cells].every(c=>c.innerText)) { document.getElementById('msg').innerText = "Berabere!"; game=false; }
            }
        </script>
        <br><a href='/oyunlar' style='color:yellow;'>Menüye Dön</a>
    </body></html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
