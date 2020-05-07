from django.test import TestCase
from english_dict.business_logic import Translator


class TranslatorTestCase(TestCase):
    def setUp(self):
        pass

    def test_tokenize(self):
        text = "I and my cats walked. Cats like to travel"
        self.assertEqual(Translator.tokenize(text),
                         ["i", "and", "my", "cats", "walked", "cats", "like", "to", "travel"])

    def test_lemmatize(self):
        text = "I and my cats walked. Cats like to travel"
        self.assertEqual(Translator.lemmatize(Translator.tokenize(text)),
                         {"i": "i", "and": "and", "my": "my", "cats": "cat", "walked": "walk", "like": "like",
                          "to": "to", "travel": "travel"})
