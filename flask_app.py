from flask import Flask, render_template, request, make_response, redirect, abort
from flask_bootstrap import Bootstrap
app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/requisition')
def requisition():
    user_agent = request.headers.get('User-Agent')
    dados = {"navegador": user_agent, "request": request}
    return render_template('requisition.html', dados = dados)


