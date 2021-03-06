from bs4 import BeautifulSoup
import requests
import re


def get_html(url_adress):
    response_html = requests.get(url_adress)
    if response_html.ok:
        return response_html.text
    else:
        return None


def parse_html(html_content):
    if html_content:
        parsed_html = BeautifulSoup(html_content, 'lxml')
        parsed_html.original_encoding
    else:
        parsed_html = None
    return parsed_html


def get_body_text(parsed_html):
    txt = parsed_html.body.get_text()
    for s in parsed_html.body.findAll('script'):
        s.decompose()
        txt = parsed_html.body.get_text()
    return txt


def find_keywords(parsed_html):
    list_all_kwords = []
    for kword_attr in parsed_html.find_all("meta", attrs={'name':re.compile('(?i)keywords')}):
        try:
            kw_content = kword_attr['content']
            kword_lst = [x.strip() for x in kw_content.split(',')]
        except Exception as e:
            kword_lst = []

        list_all_kwords.extend(kword_lst)

    return list(dict.fromkeys(list_all_kwords))


def create_dict(words):
    results = {}
    if words:
        for word in words:
            results[word] = 0
    return results


def count_words(parsed_html, words):
    result_dict = create_dict(words)
    txt = get_body_text(parsed_html)
    if words:
        for word in words:
            count = 0
            for match in re.finditer(r'(?i)\b%s\b' % re.escape(word), txt):
                count += 1
            result_dict[word] += count

    return result_dict
