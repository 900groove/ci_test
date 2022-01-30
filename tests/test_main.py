import unittest

from main import count_words


class TestCountWords(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "That that is is that that is not is not is that it it is"

    def test_count_words(self):
        c = count_words(self.text)
        self.assertTrue(isinstance(c, dict))
