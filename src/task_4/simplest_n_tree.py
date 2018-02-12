#
#   Created by Oleh Kurachenko
#          aka soll_nevermind aka okurache
#   on 2018-02-12T19:36:14Z as a part of KMA_InformationRetrieval_Dictionaty_Python3
#
#   copying code from GitHub doesn't make you smarter,
#   better ask me oleh.kurachenko@gmail.com , I'm ready to help
#
#   checkout my GitHub https://github.com/OlehKurachenko
#   rate, CV & contacts http://www.linkedin.com/in/oleh-kurachenko-6b025b111
#  


class SimplestNTree:
    # TODO write documentation
    # TODO make pretty

    def __init__(self, size):
        assert type(size) == int, SimplestNTree.__WRONG_ARGUMENT_TYPE

        self.size = size
        self.root = [False] * size

    def add_value(self, value):
        assert type(value) == str, SimplestNTree.__WRONG_ARGUMENT_TYPE

        value += chr(ord("z") + 1)
        i = 0
        node = self.root
        while i < len(value):
            if node[ord(value[i]) - ord('a')]:
                node = node[ord(value[i]) - ord('a')]
                i += 1
            else:
                break
        if i == len(value):
            return
        while i < len(value):
            node[ord(value[i]) - ord('a')] = [False] * self.size
            node = node[ord(value[i]) - ord('a')]
            i += 1

    def has_value(self, value):
        assert type(value) == str, SimplestNTree.__WRONG_ARGUMENT_TYPE

        value += chr(ord("z") + 1)
        i = 0
        node = self.root
        while i < len(value):
            if node[ord(value[i]) - ord('a')]:
                node = node[ord(value[i]) - ord('a')]
                i += 1
            else:
                break
        if i == len(value):
            return True
        return False

    __WRONG_ARGUMENT_TYPE = "Wrong argument type"
