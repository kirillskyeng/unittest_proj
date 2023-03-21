import unittest
from utils import dicts

class TestDict(unittest.TestCase):

    def test_get(self):
        self.assertEqual(dicts.get_val({"dog": "woof"}, "dog", "git"), "woof")
        self.assertEqual(dicts.get_val({"dog": "woof"}, "baa", "error"), "error")
        self.assertEqual(dicts.get_val({"dog": "woof", "frog": "ribbit"}, "frog", "git"), "ribbit")




