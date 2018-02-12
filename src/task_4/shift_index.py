#
#   Created by Oleh Kurachenko
#          aka soll_nevermind aka okurache
#   on 2018-02-12T20:58:46Z as a part of KMA_InformationRetrieval_Dictionaty_Python3
#
#   copying code from GitHub doesn't make you smarter,
#   better ask me oleh.kurachenko@gmail.com , I'm ready to help
#
#   checkout my GitHub https://github.com/OlehKurachenko
#   rate, CV & contacts http://www.linkedin.com/in/oleh-kurachenko-6b025b111
#

from src.text_file_tokenizers.text_file_simplest_tokenizer import TestFileSimplestTokenizer


class ShiftIndex:
    # TODO write documentation
    # TODO make pretty

    def __init__(self, target_files):
        self.__inverted_index = {}
        if type(target_files) == list:
            self.__files = list(target_files)
            for i, file in enumerate(target_files):
                words_gen = TestFileSimplestTokenizer(file).token_generator
                for word in words_gen:
                    i = 0
                    word += "$"
                    while i < len(word):
                        self.__inverted_index.setdefault(word, [])
                        ii_list = self.__inverted_index[word]
                        if not (ii_list and ii_list[-1] == i):
                            ii_list.append(i)
                        word = word[-1] + word[:-1]
                        i += 1
        else:
            pass  # TODO load existing incidence matrix

    # TODO add method "add file"

    def perform_request(self, request):
        pass  # TODO write