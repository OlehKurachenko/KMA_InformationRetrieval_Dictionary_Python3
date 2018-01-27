import abc


class ABCSimplestDictionary(abc.ABC):
    """
    Abstract class for simplest dictionary, which stores only distinct words
    and the number of them
    """

    @abc.abstractmethod
    def add_word(self, word):
        pass

    @abc.abstractmethod
    def export_dictionary(self, filename):
        pass

    @abc.abstractmethod
    def get_words(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass
