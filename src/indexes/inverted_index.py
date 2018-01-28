from src.indexes.abs_binary_searcher import ABSBinarySearcher
from src.text_file_tokenizers.text_file_simplest_tokenizer import TestFileSimplestTokenizer


class InvertedIndex(ABSBinarySearcher):

    def __init__(self, target_files):
        self.__inverted_index = {}
        if type(target_files) == list:
            self.__files = list(target_files)
            for i, file in enumerate(target_files):
                words_gen = TestFileSimplestTokenizer(file).token_generator
                for word in words_gen:
                    self.__inverted_index.setdefault(word, [])
                    ii_list = self.__inverted_index[word]
                    if not (ii_list and ii_list[-1] == i):
                        ii_list.append(i)
        else:
            pass #TODO load existing incidence matrix

    def export(self, filename):
        assert type(filename) == str, InvertedIndex.__WRONG_ARGUMENT_TYPE

        file = open(filename, "w+")
        file.write(
            "re_im " + str(len(self.__inverted_index)) + " " + str(
                len(self.__files)))
        for filename in self.__files:
            file.write(" " + filename)
        file.write("\n")
        for key in self.__inverted_index.keys():
            file.write(key)
            for val in self.__inverted_index[key]:
                file.write(" " + str(val))
            file.write("\n")
        file.close()

    def perform_request(self, request):
        pass # TODO write

    __WRONG_ARGUMENT_TYPE = "Wrong argument type"