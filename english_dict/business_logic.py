import nltk
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from english_dict.models import Word
nltk.download('wordnet')


class Translator:
    @staticmethod
    def __get_wordnet_pos(word):
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        return tag_dict.get(tag, wordnet.NOUN)

    @staticmethod
    def tokenize(input_text):
        input_text = re.compile("[^\w]").sub(' ', input_text)
        return nltk.word_tokenize(input_text.lower())

    @staticmethod
    def lemmatize(tokens):
        lemmatizer = WordNetLemmatizer()
        lemmas = dict()
        for w in tokens:
            if lemmas.get(w) is None:
                lemmas[w] = lemmatizer.lemmatize(w, Translator.__get_wordnet_pos(w))
        return lemmas

    @staticmethod
    def translate(input_text):
        tokens = Translator.tokenize(input_text)
        lemmas = Translator.lemmatize(tokens)
        translated_words = dict()
        for key, value in lemmas.items():
            translated_words[key] = Word.objects.get_words_by_lemma(value)
        all_translated_words = [{"token": token, "word": list(translated_words.get(token))} for token in tokens]
        return all_translated_words
