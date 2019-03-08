from bs4 import BeautifulSoup
import requests
import re

def parse_html(url):
    response_html = requests.get(url)
    if response_html.status_code != 404:
        txt_response_html = response_html.text
        parsed_html = BeautifulSoup(txt_response_html, 'lxml')
        parsed_html.original_encoding
    else:
        parsed_html = None
    return parsed_html


def remove_scripts(parsed_html):
    for s in parsed_html.body.findAll('script'):
        s.decompose()
        txt = parsed_html.body.get_text()
    return txt


def find_keywords(parsed_html):
    # pętla jeli byłoby więcej niż jeden tag meta z atrybutem keywords.
    list_all_kwords = []
    for kword_attr in parsed_html.find_all("meta", attrs={'name':re.compile('(?i)keywords')}):
        try:
            kw_content = kword_attr['content']
            kword_lst = kw_content.split(',')

        except Exception as e:
            kword_lst = []

        list_all_kwords.extend(kword_lst)

    return list(set(list_all_kwords))


def create_dict(words):
    results = {}
    if words:
        for word in words:
            results[word] = 0
    return results


def count_words(parsed_html, words):
    result_dict = create_dict(words)
    txt = remove_scripts(parsed_html)
    if words:
        for word in words:
            count = 0
            for match in re.finditer(r'(?i)\b%s\b' % re.escape(word), txt):
                count += 1
            result_dict[word] += count

    return result_dict
