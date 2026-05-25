from flask import Flask

app = Flask(__name__)

# --- ANA SAYFA ---
@app.route('/')
def ana_sayfa():
    return """
    <body style="margin:0; background-image:url('https://images.unsplash.com/photo-1506744038136-46273834b3fb'); background-size:cover; text-align:center; color:white; height:100vh; display:flex; flex-direction:column; align-items:center; justify-content:center; font-family:Arial;">
        <h1>Erkam'ın Sitesi</h1>
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
        <a href="/xox-secim" style="color:yellow; font-size:30px;">Tic Tac Toe (XOX)</a><br><br>
        <a href="/snake" style="color:green; font-size:30px;">🐍 Yılan Oyunu</a>
    </body>
    """

# --- XOX ZORLUK SEÇİMİ ---
@app.route('/xox-secim')
def xox_secim():
    return """
    <body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <a href='/oyunlar' style='position:absolute; top:10px; left:10px; font-size:40px; text-decoration:none;'>🔙</a>
        <h1>Zorluk Seç</h1>
        <a href="/xox-oyunu?mod=easy" style="color:cyan; display:block; padding:10px;">🟢 Kolay</a>
        <a href="/xox-oyunu?mod=medium" style="color:yellow; display:block; padding:10px;">🟡 Orta</a>
        <a href="/xox-oyunu?mod=hard" style="color:red; display:block; padding:10px;">🔴 Zor</a>
    </body>
    """

# --- XOX OYUN EKRANI (Müzikli) ---
@app.route('/xox-oyunu')
def xox_oyunu():
    return """
    <html><body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif;">
        <a href='/xox-secim' style='position:absolute; top:10px; left:10px; font-size:40px; text-decoration:none;'>🔙</a>
        <h1>XOX Oyunu</h1>
        <button onclick="toggleMusic()">🔊 Müzik Aç/Kapat</button>
        <audio id="bgMusic" loop src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"></audio>
        <div id="board" style="display:grid; grid-template-columns:repeat(3, 100px); gap:10px; justify-content:center; margin-top:20px;">
            <script>
                for(let i=0; i<9; i++) document.write(`<div class="c" id="${i}" onclick="p(${i})" style="width:100px; height:100px; background:white; color:black; font-size:40px; display:flex; align-items:center; justify-content:center; cursor:pointer;"></div>`);
            </script>
        </div>
        <script>
            function toggleMusic(){ let m=document.getElementById('bgMusic'); m.paused ? m.play() : m.pause(); }
            let board = Array(9).fill(null);
            const mod = new URLSearchParams(window.location.search).get('mod');
            function p(i){ if(!board[i]){ board[i]='X'; document.getElementById(i).innerText='X'; if(!check('X')) setTimeout(robot, 300); } }
            function robot(){
                let empty = board.map((v,i)=>v===null?i:null).filter(v=>v!==null);
                let move = (mod==='easy') ? empty[Math.floor(Math.random()*empty.length)] : (findWinningMove('O') || findWinningMove('X') || empty[Math.floor(Math.random()*empty.length)]);
                board[move]='O'; document.getElementById(move).innerText='O'; check('O');
            }
            function findWinningMove(p){
                const w = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
                for(let i of w){ let c=[board[i[0]],board[i[1]],board[i[2]]]; if(c.filter(x=>x===p).length===2 && c.includes(null)) return i[c.indexOf(null)]; }
                return null;
            }
            function check(p){
                const w = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
                let win = w.find(i=>board[i[0]] && board[i[0]]===board[i[1]] && board[i[1]]===board[i[2]]);
                if(win || !board.includes(null)){ setTimeout(()=>alert(win?board[win[0]]+' Kazandı!':'Berabere!'), 100); location.reload(); return true; }
                return false;
            }
        </script>
    </body></html>
    """

# --- YILAN OYUNU (Düzeltilmiş Başlatma ve Reset) ---
@app.route('/snake')
def snake():
    return """
    <html><body style="background:#2c3e50; color:white; text-align:center; font-family:sans-serif; overflow:hidden;">
        <a href='/oyunlar' style='position:absolute; top:10px; left:10px; font-size:40px; text-decoration:none;'>🔙</a>
        <h1>Yılan Oyunu</h1>
        <h2 id="scoreBoard">Puan: 0</h2>
        <button onclick="toggleMusic()">🔊 Müzik Aç/Kapat</button>
        <audio id="bgMusic" loop src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"></audio>
        <canvas id="gameCanvas" width="400" height="400" style="background:black; border:2px solid white; display:block; margin:10px auto;"></canvas>
        <div style="display:grid; grid-template-columns: 80px 80px 80px; gap:10px; justify-content:center;">
            <div></div><button id="up" style="padding:20px;">⬆️</button><div></div>
            <button id="left" style="padding:20px;">⬅️</button><button id="down" style="padding:20px;">⬇️</button><button id="right" style="padding:20px;">➡️</button>
        </div>
        <script>
            function toggleMusic(){ let m=document.getElementById('bgMusic'); m.paused ? m.play() : m.pause(); }
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");
            let snake = [{x: 200, y: 200}], dx = 0, dy = 0, food = {x: 100, y: 100}, score = 0, gameActive = false;
            
            function setDir(x,y){ 
                if(!gameActive) gameActive = true;
                if((x!=0 && dx==0) || (y!=0 && dy==0)){ dx=x; dy=y; } 
            }
            document.getElementById("up").onclick = () => setDir(0, -20);
            document.getElementById("down").onclick = () => setDir(0, 20);
            document.getElementById("left").onclick = () => setDir(-20, 0);
            document.getElementById("right").onclick = () => setDir(20, 0);
            
            function draw(){
                ctx.fillStyle = "black"; ctx.fillRect(0,0,400,400);
                ctx.fillStyle = "red"; ctx.fillRect(food.x, food.y, 20, 20);
                ctx.fillStyle = "lime";
                snake.forEach(p => ctx.fillRect(p.x, p.y, 20, 20));
                
                if(gameActive){
                    let head = {x: snake[0].x + dx, y: snake[0].y + dy};
                    snake.unshift(head);
                    if(head.x==food.x && head.y==food.y){ 
                        score+=10; document.getElementById("scoreBoard").innerText="Puan: "+score; 
                        food={x:Math.floor(Math.random()*20)*20, y:Math.floor(Math.random()*20)*20}; 
                    } else snake.pop();
                    
                    if(head.x<0||head.x>=400||head.y<0||head.y>=400){ 
                        alert("Oyun Bitti! Skor: "+score); 
                        location.reload(); 
                    }
                }
                setTimeout(draw, 100);
            }
            draw();
        </script>
    </body></html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
