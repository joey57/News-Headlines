import unittest
from app.models import News


class TestNewsSource(unittest.TestCase):
    '''
    '''
    def setUp(self):
        '''
        '''
        self.new_newssource =News('abc','liz','liz.com','lorem ipsum','kenya','technology', 'abc-news')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_newssource, News))