from word_stat_app import app
from flask import render_template, url_for, request
from word_stat_app.utils import parse_html, count_words, find_keywords, get_html


@app.route("/")
@app.route("/home")
def home():

    return render_template('home.html')


@app.route("/stats", methods=['GET'])
def stats():
    param = request.args.get('url')
    try:
        given_html = get_html(param)
        parsed_html = parse_html(given_html)
        if parsed_html is not None:
            word_list = find_keywords(parsed_html)
            dict_res = count_words(parsed_html, word_list)
            if dict_res:
                return render_template('stats.html', param=param, dict_res=dict_res)
            else:
                return render_template('errors/no_keywords.html', param=param)
        else:
            return render_template('errors/error404.html')
    except Exception as e:
        return render_template('errors/exceptions.html', e=e)
