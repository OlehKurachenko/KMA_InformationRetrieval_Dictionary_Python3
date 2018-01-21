"""
Simplest Array Dictionary
"""


class SimplestArrayDictionary:

    def __init__(self):
        self.words = []

    def add_word(self, word):
        if not (word in self.words):
            self.words.append(word)

    def __str__(self):
        res = "Words: {"
        for word in self.words:
            res += '[' + word + ']'
        res += '}'
        return res
