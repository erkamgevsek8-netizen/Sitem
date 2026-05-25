from flask import Flask

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    return """
    <html>
    <head>
        <title>Erkan'ın Sitesi</title>
        <style>
            body { 
                margin: 0; padding: 0; text-align: center; font-family: 'Arial', sans-serif;
                background-image: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb');
                background-size: cover; background-position: center; background-attachment: fixed;
                color: white; height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; 
            }
            h1 { font-size: 40px; text-shadow: 2px 2px 5px black; margin-bottom: 20px; }
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
        
        <a href="/yilan-oyunu" class="oyun-kutusu">
            <img src="https://cdn-icons-png.flaticon.com/512/3202/3202926.png" style="width: 60px; margin-bottom: 10px;">
            <span style="font-size: 20px; font-weight: bold;">Oyunlar</span>
        </a>
    </body>
    </html>
    """

@app.route('/yilan-oyunu')
def yilan_oyunu():
    return "<h1>Yılan Oyunu Buraya Gelecek</h1><a href='/'>Geri Dön</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
