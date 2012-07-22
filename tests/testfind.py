from unittest import TestCase

from mock import patch
from iperflexer.finder import find

HOME = '/home/humbert/'

def home():
    return HOME

def walk(self):
    for item in  [('/home/humbert/', [], ["cow.py",'cowdog.ini', 'pig.csv', 'sheeep.ini', 'cowboy.py'])]:
        yield item
        
class TestFind(TestCase):

    @patch('os.getcwd', home)
    @patch('os.walk',walk)
    def test_walk(self):
        matches = [HOME + item for item in 'cow.py cowboy.py'.split()]
        for output in find("cow*py"):
            self.assertIn(output, matches)
        matches = [HOME + item for item in "cowdog.ini sheeep.ini".split()]
        for output in find("*ini"):
            self.assertIn(output, matches)
        return
