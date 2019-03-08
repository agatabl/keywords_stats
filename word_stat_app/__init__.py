from flask import Flask


app = Flask(__name__)
# app.config.from_object('config')
app.config['SECRET_KEY']= 'secret'
from word_stat_app import routes
