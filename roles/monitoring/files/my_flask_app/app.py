from flask import Flask, render_template_string, request, redirect
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Counter con labels para usuario y resultado
login_counter = Counter(
    'my_flask_app_logins_total',
    'Número total de intentos de login',
    ['user', 'result']
)

HTML_TEMPLATE = '''
<!doctype html>
<html>
<head>
    <title>Login</title>
    <script>
    {% if category == 'success' and message %}
        alert("{{ message }}");
    {% endif %}
    </script>
</head>
<body style="text-align: center; margin-top: 50px;">
    <h1>Formulario de Login</h1>

    {% if category == 'failure' and message %}
        <p style="color: red; font-weight: bold;">{{ message }}</p>
    {% endif %}

    <form action="/login" method="post">
        <p>
            <input type="text"
                   name="username"
                   placeholder="Usuario"
                   required
                   value="{{ username }}">
        </p>
        <p>
            <input type="password"
                   name="password"
                   placeholder="Contraseña"
                   required
                   value="{{ password }}">
        </p>
        <button type="submit" style="padding: 10px 20px; font-size: 18px;">
            Entrar
        </button>
    </form>
    <p><a href="/metrics" target="_blank">Ver métricas</a></p>
</body>
</html>
'''

@app.route('/')
def index():
    # **Aquí** leemos msg y category de la URL
    message = request.args.get('msg', '')
    category = request.args.get('category', '')
    return render_template_string(
        HTML_TEMPLATE,
        message=message,
        category=category,
        username='',    # campos limpios al entrar por primera vez o tras éxito
        password=''
    )

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    pwd = request.form['password']

    if user == 'admin' and pwd == 'admin':
        login_counter.labels(user=user, result='success').inc()
        msg = 'Login correcto'
        # redirigimos con msg y category para que index() los capture
        return redirect(f"/?msg={msg}&category=success")
    else:
        login_counter.labels(user=user, result='failure').inc()
        msg = 'Usuario o contraseña incorrectos'
        # sin redirect: devolvemos template con ambos campos rellenos
        return render_template_string(
            HTML_TEMPLATE,
            message=msg,
            category='failure',
            username=user,
            password=pwd
        )

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
