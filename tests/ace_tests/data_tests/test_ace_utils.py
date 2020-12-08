import unittest

from ace.data import get_ace
from ace.data import get_english_resource_grammar
from ace.data import get_jacy_grammar


class TestAceUtils(unittest.TestCase):

    def test_get_ace(self):
        get_ace()

    def test_english_resource_grammar(self):
        get_english_resource_grammar()

    def test_get_jacy_grammar(self):
        get_jacy_grammar()
