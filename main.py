from flask import Flask

app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    return """
    <html>
        <head>
            <title>Erkan'ın Sitesi</title>
        </head>
        <body style="
            margin: 0;
            padding: 0;
            text-align: center;
            font-family: 'Arial', sans-serif;
            background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1000');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            height: 100vh;
            color: white;
        ">
            <div style="
                background-color: rgba(0, 0, 0, 0.4); 
                width: 100%; 
                height: 100%; 
                padding-top: 100px;
                box-sizing: border-box;
            ">
                <h1 style="
                    font-size: 32px; 
                    margin-bottom: 10px;
                    text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
                ">Erkan'ın İlk Web Sitesine Hoş Geldiniz!</h1>
                
                <p style="
                    font-size: 18px; 
                    margin-bottom: 30px;
                    text-shadow: 1px 1px 5px rgba(0,0,0,0.8);
                ">Bu site tamamen telefondan, Python ve Flask ile yapıldı.</p>
                
                <button onclick="alert('Selam Erkan! Kodun canavar gibi çalışıyor.')" style="
                    padding: 15px 35px;
                    font-size: 18px;
                    background-color: #ffffff;
                    color: #1e242b;
                    border: none;
                    border-radius: 30px;
                    cursor: pointer;
                    font-weight: bold;
                    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
                ">Bana Tıkla</button>
            </div>
        </body>
    </html>
    """
