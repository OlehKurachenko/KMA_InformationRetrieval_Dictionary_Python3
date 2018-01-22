"""
Simplest Array Dictionary
"""


class SimplestArrayDictionary:

    def __init__(self, filename=""):
        self.words = []
        if filename:
            importfile = open(filename)
            length = int(importfile.readline().split(":")[1])
            for i in range(length):
                self.words.append(importfile.readline().rstrip())
            importfile.close()

    def add_word(self, word):
        if not (word in self.words):
            self.words.append(word)

    def export_dictionary(self, filename):
        exportfile = open(filename, "w+")
        exportfile.write("words:" + str(len(self.words)) + '\n')
        for word in self.words:
            exportfile.write(word + '\n')
        exportfile.close()

    def __str__(self):
        res = "Words: {"
        for word in self.words:
            res += '[' + word + ']'
        res += '}'
        return res
