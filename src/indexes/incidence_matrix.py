from src.indexes.abs_binary_searcher import ABSBinarySearcher
from src.text_file_tokenizers.text_file_simplest_tokenizer import TestFileSimplestTokenizer


class IncidenceMatrix(ABSBinarySearcher):
    # TODO write documentation
    # TODO for all the project, split opening and reading (or not)

    def __init__(self, target_files):
        # assert type(use_array == bool), IncidenceMatrix.__WRONG_ARGUMENT_TYPE

        self.__incident_matrix = {}
        if type(target_files) == list:
            self.__files = target_files
            for i, file in enumerate(target_files):
                words_gen = TestFileSimplestTokenizer(file).token_generator
                for word in words_gen:
                    self.__incident_matrix.setdefault(word, [False] * len(target_files))
                    self.__incident_matrix[word][i] = True
        else:
            pass  # TODO load existing incidence matrix

    def export(self, filename):
        assert type(filename) == str, IncidenceMatrix.__WRONG_ARGUMENT_TYPE

        file = open(filename, "w+")
        file.write(
            "re_im " + str(len(self.__incident_matrix)) + " " + str(
                len(self.__files)))
        for filename in self.__files:
            file.write(" " + filename)
        file.write("\n")
        for key in self.__incident_matrix.keys():
            file.write(key + " ")
            for val in self.__incident_matrix[key]:
                file.write("1" if val else "0")
            file.write("\n")
        file.close()

    # TODO add method "add file"

    def perform_request(self, request):
        pass  # TODO write

    __WRONG_ARGUMENT_TYPE = "Wrong argument type"
