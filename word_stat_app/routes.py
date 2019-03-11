from word_stat_app import app
from flask import render_template, url_for, request
from word_stat_app.stats.stats_controller import get_stats


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/stats", methods=['GET'])
def stats():
    param = request.args.get('url')

    return get_stats(param)
