import abc


class ABSBinarySearcher(abc.ABC):
    """
    ABSBinarySearcher declares a method perform_request takes a string argument which
    is a binary search request and returns a list of files as result
    """

    @abc.abstractmethod
    def perform_request(self, request):
        pass
