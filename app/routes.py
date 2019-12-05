from flask import render_template
from app import app
import pandas as pd

data = pd.read_csv('data/predicoes.csv')

@app.route('/')
@app.route('/index')
def index():
    params = {
        'fila': 'Conta Corrente',
        'data': data
    }
    return render_template('index.html', title='Home', params=params)
