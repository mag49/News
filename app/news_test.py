import unittest
from models import news
Movie = movie.Movie

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'Aljazera News', 'Your trusted source of world news, politics,headlines, and interviews at AljazeraNews.com.","https://aljazeranews.go.com","general",' )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()