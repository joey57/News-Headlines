import unittest
from app.models import News

class TestNews(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_news_source = News('123','Misha','https://123.com/','123 news is the best source', 'london', 'general', '123-news')

    def test_instance(self):
        '''
        '''
        self.assertTrue(isinstance(self.new_news_source,News))

    def test_to_check_instance_variables(self):
        '''
        '''
        self.assertEquals(self.new_news_source.name,'123')
        self.assertEquals(self.new_news_source.author,'Misha')
        self.assertEquals(self.new_news_source.url,'https://123.com/')
        self.assertEquals(self.new_news_source.description,'123 news is the best source')
        self.assertEquals(self.new_news_source.country,'london')
        self.assertEquals(self.new_news_source.category,'general')
        self.assertEquals(self.new_news_source.id,'123-news')
