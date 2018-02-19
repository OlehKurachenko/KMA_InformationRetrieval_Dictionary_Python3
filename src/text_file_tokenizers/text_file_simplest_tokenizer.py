"""
Simplest file tokenizer
"""

from re import split

class TextFileSimplestTokenizer:

    @staticmethod
    def __lazy_line_generator(filename):
        assert type(filename) == str, TextFileSimplestTokenizer.WRONG_ARGUMENT_TYPE_MESSAGE

        with open(filename) as file:
            for line in file:
                strsplit = split("[ .,!?:;\"'\t\r\n\v\f]+", line)
                for token in strsplit:
                    if token:
                        yield token.lower()

    def __init__(self, filename):
        assert type(filename) == str, TextFileSimplestTokenizer.WRONG_ARGUMENT_TYPE_MESSAGE

        self._token_generator = TextFileSimplestTokenizer.__lazy_line_generator(filename)

    @property
    def token_generator(self):
        return self._token_generator

    WRONG_ARGUMENT_TYPE_MESSAGE = "Wrong argument type"
