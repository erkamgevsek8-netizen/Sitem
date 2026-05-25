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
            h1 { font-size: 40px; text-shadow: 2px 2px 5px black; }
        </style>
    </head>
    <body>
        <h1>Erkan'ın Web Sitesine Hoş Geldiniz!</h1>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
