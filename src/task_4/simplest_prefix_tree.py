#
#   Created by Oleh Kurachenko
#          aka soll_nevermind aka okurache
#   on 2018-02-12T19:32:34Z as a part of KMA_InformationRetrieval_Dictionaty_Python3
#
#   copying code from GitHub doesn't make you smarter,
#   better ask me oleh.kurachenko@gmail.com , I'm ready to help
#
#   checkout my GitHub https://github.com/OlehKurachenko
#   rate, CV & contacts http://www.linkedin.com/in/oleh-kurachenko-6b025b111
#  

from src.task_4.simplest_n_tree import SimplestNTree

class SimplestPrefixTree:
    # TODO write documentation
    # TODO make pretty

    def __init__(self):
        self.tree = SimplestNTree(ord("z") - ord("a") + 2)

    def add_word(self, word):
        self.tree.add_value(word)

    def has_word(self, word):
        self.tree.has_value(word)
