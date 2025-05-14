from flask import Flask, render_template_string, redirect
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

click_counter = Counter('my_flask_app_clicks_total', 'Número total de clics')

HTML_TEMPLATE = '''
<!doctype html>
<html>
<head>
    <title>Contador de Clics</title>
</head>
<body style="text-align: center; margin-top: 50px;">
    <h1>¡Bienvenido a My Flask App!</h1>
    <form action="/click" method="post">
        <button style="padding: 10px 20px; font-size: 18px;">Haz clic</button>
    </form>
    <p><a href="/metrics" target="_blank">Ver métricas</a></p>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/click', methods=['POST'])
def click():
    click_counter.inc()
    return redirect('/')

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
