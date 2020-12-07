import unittest

from ace.paraphrase import generate_paraphrase


class TestParaphrase(unittest.TestCase):

    def test_generate_paraphrase(self):
        text = 'This person opens a door.'
        paraphrase_list = generate_paraphrase(text)
        self.assertEqual(paraphrase_list[0],
                         'This person opens a door.')
        self.assertEqual(paraphrase_list[1],
                         'A door is opened by this person.')
