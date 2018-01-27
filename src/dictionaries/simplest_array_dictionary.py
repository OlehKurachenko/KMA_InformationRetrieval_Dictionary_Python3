from src.dictionaries.abc_simplest_dictionary import ABCSimplestDictionary
import collections


class SimplestArrayDictionary(ABCSimplestDictionary):
    """
    Stores distinct words in list
    """

    def __init__(self, filename=""):
        assert type(filename) == str, ABCSimplestDictionary.WRONG_ARGUMENT_TYPE_MESSAGE

        self.words = []
        if filename:
            # TODO protect from wrong file
            importfile = open(filename)
            length = int(importfile.readline().split(":")[1])
            for i in range(length):
                self.words.append(importfile.readline().rstrip())
            importfile.close()

    def add_word(self, word):
        assert type(word) == str, ABCSimplestDictionary.WRONG_ARGUMENT_TYPE_MESSAGE

        if not (word in self.words):
            self.words.append(word)

    def add_words(self, words):
        assert isinstance(words,
                          collections.Iterable), ABCSimplestDictionary.WRONG_ARGUMENT_TYPE_MESSAGE
        for word in words:
            assert type(word) == str, ABCSimplestDictionary.WRONG_ARGUMENT_TYPE_MESSAGE

        for word in words:
            self.add_word(word)

    def export_dictionary(self, filename):
        assert type(filename) == str, ABCSimplestDictionary.WRONG_ARGUMENT_TYPE_MESSAGE

        exportfile = open(filename, "w+")
        exportfile.write("words:" + str(len(self.words)) + '\n')
        for word in self.words:
            exportfile.write(word + '\n')
        exportfile.close()

    def get_words(self):
        return tuple(self.words)

    def __str__(self):
        res = "Words: {"
        for word in self.words:
            res += '[' + word + ']'
        res += '}'
        return res
