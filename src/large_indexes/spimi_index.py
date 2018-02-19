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


# noinspection PyUnresolvedReferences
class SPIMIndex:
    # TODO write docs
    def __init__(self, documents: "list of str", log_ostream: io.IOBase = False):
        assert type(documents) == list, SPIMIndex.WRONG_ARGUMENT_TYPE_MESSAGE
        assert len(list(filter(lambda x: type(x) != str,
                               documents))) == 0, SPIMIndex.WRONG_ARGUMENT_TYPE_MESSAGE
        assert not log_ostream or (isinstance(log_ostream, io.IOBase) and log_ostream.writable()), \
            SPIMIndex.WRONG_ARGUMENT_TYPE_MESSAGE

        self.__log_ostream = log_ostream
        self.__documents = documents
        self.__log_ostream.write()
        # TODO add dynamic block size
        # TODO finish method

    def __term_doc_pairs_generator(self):
        # TODO write

    WRONG_ARGUMENT_TYPE_MESSAGE = "Wrong argument type"
    DEFAULT_BLOCK_SIZE = 1024 * 1024
