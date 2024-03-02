from flask import Flask, render_template, request, make_response, redirect, abort
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    current_time = datetime.utcnow()
    return render_template('home.html', current_time = current_time)


@app.route('/student/<name>/<registration>/<institution>')
def student(name, registration, institution):
    return render_template('student.html', name=name, registration=registration, institution=institution)


@app.route('/requisition/<name>')
def requisition(name):
    user_agent = request.headers.get('User-Agent')
    dados = {"navegador": user_agent, "request": request, "name": name}
    return render_template('requisition.html', dados = dados)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

