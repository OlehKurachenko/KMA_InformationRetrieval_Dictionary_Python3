#
#   Created by Oleh Kurachenko
#          aka soll_nevermind aka okurache
#   on 2018-02-16T09:43:40Z as a part of KMA_InformationRetrieval_Dictionaty_Python3
#
#   ask     oleh.kurachenko@gmail.com , I'm ready to help
#   GitHub  https://github.com/OlehKurachenko
#   rate&CV http://www.linkedin.com/in/oleh-kurachenko-6b025b111
#  

import io
import sys
import time
import os
from functools import reduce
from src.text_file_tokenizers.text_file_simplest_tokenizer import TextFileSimplestTokenizer


# noinspection PyUnresolvedReferences
class SPIMIndex:
    # TODO write docs
    def __init__(self, documents: "list of str", log_ostream: io.IOBase = False):
        # TODO write logs
        assert type(documents) == list, SPIMIndex.WRONG_ARGUMENT_TYPE_MESSAGE
        assert len(list(filter(lambda x: type(x) != str,
                               documents))) == 0, SPIMIndex.WRONG_ARGUMENT_TYPE_MESSAGE
        assert not log_ostream or (isinstance(log_ostream, io.IOBase) and log_ostream.writable()), \
            SPIMIndex.WRONG_ARGUMENT_TYPE_MESSAGE

        self.__log_ostream = log_ostream
        self.__documents = documents
        # TODO: log self.__log_ostream.write()
        self.__id = int(time.time())
        self.__dirname = "data/spimi/" + str(self.__id)
        self.__file_id = 1
        # TODO move constant to static
        os.makedirs(self.__dirname)
        self.__blocks = []
        # TODO add dynamic block size
        self.__block_size = SPIMIndex.DEFAULT_BLOCK_SIZE

        block_size = 0
        block = []

        for term_pair in self.__term_doc_pairs_generator():
            block.append(term_pair)
            block_size += SPIMIndex.DEFAULT_EMPTY_STR_SIZE + SPIMIndex.DEFAULT_INT_SIZE + len(
                term_pair)
            if block_size > self.__block_size:
                block.sort()
                self.__export_block(block)
                block = []
                block_size = 0

        self.index_name = reduce(lambda file1, file2: self.__merge_blockfiles(file1, file2),
                                   self.__blocks)

    def __term_doc_pairs_generator(self):
        for document_id, document in enumerate(self.__documents):
            for word in TextFileSimplestTokenizer(document).token_generator:
                yield (word, document_id)

    def __export_block(self, block: "list of tuples"):
        self.__blocks.append(self.__dirname + "/block_" + str(self.__file_id) + ".txt")
        self.__file_id += 1
        with open(self.__blocks[-1], "w+") as export_file:
            for tup in block:
                export_file.write(tup[0] + " " + str(tup[1]) + "\n")

    def __merge_blockfiles(self, file1: str, file2: str):
        new_blockfile_name = self.__dirname + "/block_" + str(self.__file_id) + "m.txt"
        self.__file_id += 1
        with open(file1, "r") as file_1:
            with open(file2, "r") as file_2:
                with open(new_blockfile_name, "w+") as new_blockfile:
                    file1_line = file_1.readline()
                    file2_line = file_2.readline()
                    while file1_line and file2_line:
                        if file1_line < file2_line:
                            new_blockfile.write(file1_line)
                            file1_line = file_1.readline()
                        else:
                            new_blockfile.write(file2_line)
                            file2_line = file_2.readline()
                    while file1_line:
                        new_blockfile.write(file1_line)
                        file1_line = file_1.readline()
                    while file2_line:
                        new_blockfile.write(file2_line)
                        file2_line = file_2.readline()
                    return new_blockfile_name

    WRONG_ARGUMENT_TYPE_MESSAGE = "Wrong argument type"
    DEFAULT_BLOCK_SIZE = 1024 * 1024
    DEFAULT_EMPTY_STR_SIZE = sys.getsizeof("")
    DEFAULT_INT_SIZE = sys.getsizeof(DEFAULT_BLOCK_SIZE)
