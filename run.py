from flask import Flask, render_template, request

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('base.html')

@app.route('/inversion/')
def inversion_list():
    inversion_list = [200,400,600,543]
    context = {'inversion_list':inversion_list}
    return render_template('inversion/inversion_list.html', **context)