#
#   Created by Oleh Kurachenko
#          aka soll_nevermind aka okurache
#   on 2018-02-12T21:14:48Z as a part of KMA_InformationRetrieval_Dictionaty_Python3
#
#   copying code from GitHub doesn't make you smarter,
#   better ask me oleh.kurachenko@gmail.com , I'm ready to help
#
#   checkout my GitHub https://github.com/OlehKurachenko
#   rate, CV & contacts http://www.linkedin.com/in/oleh-kurachenko-6b025b111
#  

from src.text_file_tokenizers.text_file_simplest_tokenizer import TestFileSimplestTokenizer


class TrigrammIndex:
    # TODO write documentation
    # TODO make pretty

    def __init__(self, target_files):
        self.__inverted_index = {}
        if type(target_files) == list:
            self.__files = list(target_files)
            for i, file in enumerate(target_files):
                words_gen = TestFileSimplestTokenizer(file).token_generator
                for word in words_gen:
                    word = "$" + word + "$"
                    i = 0
                    while i < len(word - 2):
                        temp_word = word[i:i+3]
                        self.__inverted_index.setdefault(temp_word, [])
                        ii_list = self.__inverted_index[temp_word]
                        if not (ii_list and ii_list[-1] == i):
                            ii_list.append(i)
        else:
            pass  # TODO load existing incidence matrix

    # TODO optimize
    def perform_request(self, request):
        assert type(request) == str, TrigrammIndex.__WRONG_ARGUMENT_TYPE

        request = "$" + request + "$"

        resq = "$"

        i = 0
        while i < len(request) - 2:
            temp = request[i:i+3]
            i += 1
            if temp[0] == "*" or temp[0] == "*" or temp[0] == "*":
                continue
            resq += " and " + temp

        request = resq

        request += ' '
        words_list = []
        operations_list = []
        i = 0
        is_value = True
        while i < len(request):
            while i < len(request) and request[i] == ' ' :
                i += 1
            if i == len(request):
                break
            if request[i] == '(':
                operations_list.append('(')
                i += 1
            elif request[i] == ')':
                temp_opp = operations_list.pop()
                while temp_opp != '(':
                    if temp_opp == 'or':
                        words_list.append(
                            TrigrammIndex.lists_merge(words_list.pop(), words_list.pop()))
                    elif temp_opp == 'and':
                        words_list.append(
                            TrigrammIndex.lists_intersect(words_list.pop(), words_list.pop()))
                    else:
                        raise Exception
                    temp_opp = operations_list.pop()
                i += 1
            else:
                j = i
                while request[j] != ' ':
                    j += 1
                word = request[i:j]
                i = j
                if is_value:
                    if word in self.__inverted_index:
                        words_list.append(self.__inverted_index[word])
                    else:
                        words_list.append([])
                else:
                    operations_list.append(word)
                is_value = not is_value
        while operations_list:
            temp_opp = operations_list.pop()
            if temp_opp == 'or':
                words_list.append(
                    TrigrammIndex.lists_merge(words_list.pop(), words_list.pop()))
            elif temp_opp == 'and':
                words_list.append(
                    TrigrammIndex.lists_intersect(words_list.pop(), words_list.pop()))
            else:
                print(temp_opp)
                raise Exception
        if len(words_list) != 1 or operations_list:
            raise Exception
        res = []
        for i in words_list.pop():
            res.append(self.__files[i])
        return res

    @staticmethod
    def lists_merge(l1, l2):
        assert type(l1) == list, TrigrammIndex.__WRONG_ARGUMENT_TYPE
        assert type(l2) == list, TrigrammIndex.__WRONG_ARGUMENT_TYPE

        lr = []
        i1 = 0
        i2 = 0
        while i1 < len(l1) and i2 < len(l2):
            if l1[i1] == l2[i2]:
                lr.append(l1[i1])
                i1 += 1
                i2 += 1
            elif l1[i1] > l2[i2]:
                lr.append(l2[i2])
                i2 += 1
            else:
                lr.append(l1[i1])
                i1 += 1
        while i1 < len(l1):
            lr.append(l1[i1])
            i1 += 1
        while i2 < len(l2):
            lr.append(l2[i2])
            i2 += 1
        return lr

    @staticmethod
    def lists_intersect(l1, l2):
        assert type(l1) == list, TrigrammIndex.__WRONG_ARGUMENT_TYPE
        assert type(l2) == list, TrigrammIndex.__WRONG_ARGUMENT_TYPE

        lr = []
        i1 = 0
        i2 = 0
        while i1 < len(l1) and i2 < len(l2):
            if l1[i1] == l2[i2]:
                lr.append(l1[i1])
                i1 += 1
                i2 += 1
            elif l1[i1] > l2[i2]:
                i2 += 1
            else:
                i1 += 1
        return lr

    __WRONG_ARGUMENT_TYPE = "Wrong argument type"