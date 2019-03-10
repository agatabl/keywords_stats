import unittest
from unittest.mock import  patch
import utils
from bs4 import BeautifulSoup


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.html_kw = """<html><head><meta charset="utf-8">
                            <meta name="keywords" content="Some, dummy keywords, for, testing">
                            </head>
                            <body>There are some dummy keywords
                            <div class"testing">Just for testing
                            <p>Some, some, for testing keywords</p></div></body>
                            <sript>wsedfg </script> </html>"""

        self.html_no_kw = """ <html><head>
                                <meta charset="utf-8">
                                <title>Lorem ipsum dolor sit amet, consectetur adipisicing elit.</title>
                            </head><body>There are some dummy keywords
                            <div class"testing">Just for testing
                            <p>Some, some, for testing keywords</p></div></body></html>"""



        self.words = ['Some', 'dummy keywords', 'for','testing']
        self.result_dict = {'Some':0, 'dummy keywords':0, 'for':0, 'testing':0}

    def tearDown(self):
        pass

    def test_get_html_check_connection(self):
        self.assertIsNotNone(utils.get_html('http://www.example.org'))

    def test_get_html_(self):
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.text = "Succes"
            response = utils.get_html('justsomeadress')
            mock_get.assert_called_with('justsomeadress')
            self.assertEqual(response, "Succes")

            mock_get.return_value.ok = False
            response = utils.get_html('anothereadress')
            mock_get.assert_called_with('anothereadress')
            self.assertEqual(response, None)


    def test_parse_html(self):
        self.assertIsNotNone(utils.parse_html(self.html_kw))
        self.assertIsNotNone(utils.parse_html(self.html_no_kw))

    def test_find_keywords(self):
        parsed_html_kw = BeautifulSoup(self.html_kw, 'lxml')
        parsed_html_no_kw = BeautifulSoup(self.html_no_kw, 'lxml')

        self.assertListEqual(utils.find_keywords(parsed_html_kw), self.words)
        self.assertListEqual(utils.find_keywords(parsed_html_no_kw),[])

    def test_create_dict(self):
        self.assertDictEqual(utils.create_dict(self.words), self.result_dict)


    def test_count_words(self):
        html_body = """There are some dummy keywords Just for testing Some, some, for testing keywords"""
        with patch ('utils.create_dict') as mock_dict,\
            patch ('utils.get_body_text') as mock_text:
            mock_dict.return_value = self.result_dict
            mock_text.return_value = html_body

            self.assertDictEqual(utils.count_words('whatever',self.words),
             {'Some':3, 'dummy keywords':1, 'for':2, 'testing':2} )


    def test_get_body_text(self):
        parsed_html_kw = BeautifulSoup(self.html_kw, 'lxml')
        parsed_html_no_kw = BeautifulSoup(self.html_no_kw, 'lxml')


        self.assertEqual(utils.get_body_text(parsed_html_kw), parsed_html_no_kw.body.get_text())
        self.assertEqual(utils.get_body_text(parsed_html_no_kw), parsed_html_no_kw.body.get_text())

if __name__ == '__main__':
    unittest.main()
