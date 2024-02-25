from flask import Flask, render_template
app = Flask(__name__,
            static_url_path='', 
            static_folder='static',)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/requisition')
def requisition():
    return render_template('requisition.html')


