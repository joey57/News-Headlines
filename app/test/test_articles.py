import unittest
from app.models import Articles

class TestArticle(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.new_article =Articles('abc','lorem ipsum','image','12-24-2018','liz','abc.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))    


    