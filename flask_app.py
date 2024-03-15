from flask import Flask, render_template, request, redirect, session, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CHAVE BRABA'

bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('Informe o seu nome', validators=[DataRequired()])
    surname = StringField('Informe o seu sobrenome:', validators=[DataRequired()])
    institution = StringField('Informe a sua Insituição de ensino:', validators=[DataRequired()])
    discipline = SelectField(u'Informe a sua disciplina:', choices=[('dswa5', 'DSWA5'), ('dwba4', 'DWBA4'), ('GPSA5', 'Gestão de projetos')])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def home():
    current_time = datetime.utcnow()
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Você alterou o seu nome!')
        session['name'] = form.name.data
        session['surname'] = form.surname.data
        session['institution'] = form.institution.data
        session['discipline'] = form.discipline.data
        session['remote_addr'] = request.remote_addr
        session['host'] = request.host
        return redirect(url_for('home'))

    return render_template('home.html', 
                           form=form, 
                           name=session.get('name'), 
                           surname=session.get('surname'),
                           institution=session.get('institution'),
                           discipline=session.get('discipline'),
                           choices=dict(form.discipline.choices),
                           remote_addr=session.get('remote_addr'),
                           remote_host=session.get('host'),
                           current_time=current_time)


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

