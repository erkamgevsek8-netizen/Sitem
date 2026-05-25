from flask import Flask

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    return """
    <body style="margin:0; background-image:url('https://images.unsplash.com/photo-1506744038136-46273834b3fb'); background-size:cover; text-align:center; color:white; height:100vh; display:flex; flex-direction:column; align-items:center; justify-content:center; font-family:Arial;">
        <h1>Erkan'ın Web Sitesine Hoş Geldiniz!</h1>
        <a href="/oyunlar" style="text-decoration:none; color:white; background:rgba(255,255,255,0.2); padding:20px; border-radius:20px; border:2px solid white; backdrop-filter:blur(10px);">
            <span style="font-size:20px; font-weight:bold;">Oyunlar</span>
        </a>
    </body>
    """

@app.route('/oyunlar')
def oyunlar():
    return """
    <body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <h1>Oyun Seçiniz</h1>
        <a href="/xox-secim" style="color:yellow; font-size:30px;">Tic Tac Toe (XOX)</a><br><br>
        <a href='/' style='color:white;'>Geri Dön</a>
    </body>
    """

@app.route('/xox-secim')
def xox_secim():
    return """
    <body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <h1>Nasıl Oynamak İstersin?</h1>
        <a href="/xox-oyunu?mod=2player" style="color:white; font-size:25px; display:block; padding:10px;">👥 2 Kişilik</a>
        <a href="/xox-oyunu?mod=robot" style="color:cyan; font-size:25px; display:block; padding:10px;">🤖 Robotla Oyna</a>
    </body>
    """

@app.route('/xox-oyunu')
def xox_oyunu():
    return """
    <html><body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <h1 id="title">Tic Tac Toe</h1>
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
        <script>
            let t='X', game=true;
            const params = new URLSearchParams(window.location.search);
            const mod = params.get('mod');
            function p(c){
                if(!c.innerText && game){
                    c.innerText=t;
                    if(check()){ game=false; return; }
                    t=t==='X'?'O':'X';
                    if(mod==='robot' && t==='O') setTimeout(robotMove, 500);
                }
            }
            function robotMove(){
                let cells = document.querySelectorAll('.cell');
                let empty = [...cells].filter(c=>!c.innerText);
                if(empty.length>0){ empty[Math.floor(Math.random()*empty.length)].innerText='O'; check(); t='X'; }
            }
            function check(){
                let c = document.querySelectorAll('.cell');
                let w = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
                for(let i of w){
                    if(c[i[0]].innerText && c[i[0]].innerText===c[i[1]].innerText && c[i[1]].innerText===c[i[2]].innerText){
                        alert(c[i[0]].innerText + " Kazandı!"); return true;
                    }
                }
                if([...c].every(x=>x.innerText)) { alert("Berabere!"); return true; }
            }
        </script>
        <br><br><a href='/xox-secim' style='color:yellow;'>Seçim Ekranına Dön</a>
    </body></html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
