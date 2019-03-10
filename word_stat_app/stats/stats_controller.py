from word_stat_app.stats.stats_utils import parse_html, count_words, find_keywords, get_html
from flask import render_template


def get_stats(url):
    try:
        given_html = get_html(url)
        parsed_html = parse_html(given_html)
        if parsed_html is not None:
            word_list = find_keywords(parsed_html)
            dict_res = count_words(parsed_html, word_list)
            if dict_res:
                return render_template('stats.html', param=url, dict_res=dict_res)
            else:
                return render_template('errors/no_keywords.html', param=url)
        else:
            return render_template('errors/error404.html')
    except Exception as e:
        return render_template('errors/exceptions.html', e=e)
