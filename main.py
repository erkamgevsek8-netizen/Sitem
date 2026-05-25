from flask import Flask

app = Flask(__name__)

# --- ANA SAYFA (Resim ve Logon Değişmedi) ---
@app.route('/')
def ana_sayfa():
    return """
    <body style="margin:0; background-image:url('https://images.unsplash.com/photo-1506744038136-46273834b3fb'); background-size:cover; text-align:center; color:white; height:100vh; display:flex; flex-direction:column; align-items:center; justify-content:center; font-family:Arial;">
        <h1>Erkan'ın Web Sitesine Hoş Geldiniz!</h1>
        <a href="/oyunlar" style="text-decoration:none; color:white; background:rgba(255,255,255,0.2); padding:20px; border-radius:20px; border:2px solid white; backdrop-filter:blur(10px);">
            <img src="https://cdn-icons-png.flaticon.com/512/3202/3202926.png" style="width:60px; margin-bottom:10px;"><br>
            <span style="font-size:20px; font-weight:bold;">Oyunlar</span>
        </a>
    </body>
    """

# --- OYUN MENÜSÜ ---
@app.route('/oyunlar')
def oyunlar():
    return """
    <body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <h1>Oyun Seçiniz</h1>
        <a href="/xox-secim" style="color:yellow; font-size:30px;">Tic Tac Toe (XOX)</a><br><br>
        <a href='/' style='color:white;'>Geri Dön</a>
    </body>
    """

# --- ZORLUK SEÇİMİ ---
@app.route('/xox-secim')
def xox_secim():
    return """
    <body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <h1>Zorluk Seç</h1>
        <a href="/xox-oyunu?mod=2player" style="color:white; display:block; padding:10px;">👥 2 Kişilik</a>
        <a href="/xox-oyunu?mod=easy" style="color:cyan; display:block; padding:10px;">🤖 Kolay Robot</a>
        <a href="/xox-oyunu?mod=hard" style="color:red; display:block; padding:10px;">🔥 ZOR (Yenilmez) Robot</a>
    </body>
    """

# --- OYUN EKRANI ---
@app.route('/xox-oyunu')
def xox_oyunu():
    return """
    <html><body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <h1>Tic Tac Toe</h1>
        <div id="board" style="display:grid; grid-template-columns:repeat(3, 100px); gap:10px; justify-content:center;">
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
            function p(i){
                if(!board[i]){
                    board[i] = 'X'; document.getElementById(i).innerText = 'X';
                    if(!check('X') && mod !== '2player') setTimeout(robot, 300);
                }
            }
            function robot(){
                let move = (mod === 'hard') ? bestMove() : board.map((v,i)=>v===null?i:null).filter(v=>v!==null)[0];
                board[move] = 'O'; document.getElementById(move).innerText = 'O';
                check('O');
            }
            function bestMove(){
                for(let i=0; i<9; i++){
                    if(!board[i]){ board[i]='O'; if(checkWinner()==='O'){ board[i]='O'; return i; } board[i]=null; }
                }
                return board.map((v,i)=>v===null?i:null).filter(v=>v!==null)[0];
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
        <br><br><a href='/xox-secim' style='color:yellow;'>Geri Dön</a>
    </body></html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
