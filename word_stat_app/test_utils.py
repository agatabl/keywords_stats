import unittest
import utils


class TestUtils(unittest.TestCase):


    url_kw = "https://www.esri.com/esri-news/arcuser/summer-2013/making-census-data-more-useful"
    url_no_kw = "http://adventuresport.pl/category/bno/"
    url_404 = "http://adventuresport.pl/category/dosnotexist/bno/asdfg"


    def test_parse_html(self):
        self.assertIsNone(utils.parse_html(self.url_404))
        self.assertIsNotNone(utils.parse_html(self.url_kw))
        self.assertIsNotNone(utils.parse_html(self.url_no_kw))

    # def test_remove_scripts(self):
    #     parsed_html = utils.parse_html(TestUtils.url_no_kw)
    #
    #     self.assertMultiLineEqual(utils.remove_scripts(parsed_html),result)

    def test_find_keywords(self):
        self.assertListEqual(utils.find_keywords(utils.parse_html(self.url_kw)),
        ['Republic of Poland Geostatistics Portal', 'ArcGIS Census', 'Poland Spatial Data Infrastructure', 'ArcGIS for Server Poland', 'Central Statistics Office of Poland'])
        self.assertListEqual(utils.find_keywords(utils.parse_html(self.url_no_kw)),[])


if __name__ == '__main__':
    unittest.main()
