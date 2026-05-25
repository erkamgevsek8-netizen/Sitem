from flask import Flask

app = Flask(__name__)

# --- ANA SAYFA ---
@app.route('/')
def ana_sayfa():
    return """
    <body style="margin:0; background-image:url('https://images.unsplash.com/photo-1506744038136-46273834b3fb'); background-size:cover; text-align:center; color:white; height:100vh; display:flex; flex-direction:column; align-items:center; justify-content:center; font-family:Arial;">
        <h1>Erkan'ın Sitesi</h1>
        <a href="/oyunlar" style="text-decoration:none; color:white; background:rgba(255,255,255,0.2); padding:20px; border-radius:20px; border:2px solid white; backdrop-filter:blur(10px);">
            <img src="https://cdn-icons-png.flaticon.com/512/3202/3202926.png" style="width:60px;"><br>Oyunlar
        </a>
    </body>
    """

# --- OYUN MENÜSÜ ---
@app.route('/oyunlar')
def oyunlar():
    return """
    <body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <a href='/' style='position:absolute; top:10px; left:10px; font-size:40px; text-decoration:none;'>🏠</a>
        <h1>Oyun Seçiniz</h1>
        <a href="/xox-secim" style="color:yellow; font-size:30px;">Tic Tac Toe (XOX)</a>
    </body>
    """

# --- ZORLUK SEÇİMİ ---
@app.route('/xox-secim')
def xox_secim():
    return """
    <body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <a href='/' style='position:absolute; top:10px; left:10px; font-size:40px; text-decoration:none;'>🏠</a>
        <h1>Zorluk Seç</h1>
        <a href="/xox-oyunu?mod=easy" style="color:cyan; display:block; padding:10px;">🟢 Seviye 1 (Kolay)</a>
        <a href="/xox-oyunu?mod=medium" style="color:yellow; display:block; padding:10px;">🟡 Seviye 2 (Orta)</a>
        <a href="/xox-oyunu?mod=hard" style="color:red; display:block; padding:10px;">🔴 Seviye 3 (Zor)</a>
    </body>
    """

# --- OYUN EKRANI ---
@app.route('/xox-oyunu')
def xox_oyunu():
    return """
    <html><body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <a href='/' style='position:absolute; top:10px; left:10px; font-size:40px; text-decoration:none;'>🏠</a>
        <h1>XOX Oyunu</h1>
        <button onclick="toggleMusic()" style="padding:10px; cursor:pointer; margin-bottom:10px;">🔊 Müzik Aç/Kapat</button>
        <audio id="bgMusic" loop src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"></audio>
        
        <div id="board" style="display:grid; grid-template-columns:repeat(3, 100px); gap:10px; justify-content:center; margin-top:20px;">
            <div class="c" id="0" onclick="p(0)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="c" id="1" onclick="p(1)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="c" id="2" onclick="p(2)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="c" id="3" onclick="p(3)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="c" id="4" onclick="p(4)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="c" id="5" onclick="p(5)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="c" id="6" onclick="p(6)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="c" id="7" onclick="p(7)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
            <div class="c" id="8" onclick="p(8)" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>
        </div>
        <script>
            let board = Array(9).fill(null);
            const mod = new URLSearchParams(window.location.search).get('mod');
            function toggleMusic(){ let m=document.getElementById('bgMusic'); m.paused ? m.play() : m.pause(); }
            function p(i){
                if(!board[i]){
                    board[i] = 'X'; document.getElementById(i).innerText = 'X';
                    if(!check('X')) setTimeout(robot, 300);
                }
            }
            function robot(){
                let empty = board.map((v,i)=>v===null?i:null).filter(v=>v!==null);
                let move;
                if(mod==='easy') move = empty[Math.floor(Math.random()*empty.length)];
                else if(mod==='medium') {
                    move = findWinningMove('O') || empty[Math.floor(Math.random()*empty.length)];
                } else {
                    move = findWinningMove('O') || findWinningMove('X') || empty[Math.floor(Math.random()*empty.length)];
                }
                board[move] = 'O'; document.getElementById(move).innerText = 'O';
                check('O');
            }
            function findWinningMove(p){
                const w = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
                for(let i of w){
                    let cells = [board[i[0]], board[i[1]], board[i[2]]];
                    if(cells.filter(c=>c===p).length===2 && cells.includes(null)) return i[cells.indexOf(null)];
                }
                return null;
            }
            function checkWinner(){
                const w = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
                for(let i of w){
                    if(board[i[0]] && board[i[0]]===board[i[1]] && board[i[1]]===board[i[2]]) return board[i[0]];
                }
                return board.includes(null) ? null : 'Tie';
            }
            function check(p){
                let res = checkWinner();
                if(res) { setTimeout(()=>alert(res==='Tie'?'Berabere!':res+' Kazandı!'), 100); location.reload(); return true; }
                return false;
            }
        </script>
    </body></html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
