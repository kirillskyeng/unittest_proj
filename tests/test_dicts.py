import unittest
from utils import dicts

class TestDict(unittest.TestCase):

    def test_get(self):
        self.assertEqual(dicts.get_val({"baba": "you"}, "baba", "git"), "you")
        self.assertEqual(dicts.get_val({"baba": "you"}, "hehe", "error"), "error")
        self.assertEqual(dicts.get_val({"baba": "you", "life": "pain"}, "life", "git"), "pain")




