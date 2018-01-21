from src import textFileSimplestTokenizer, simplestArrayDictionary

def main():
    print("Test")

    # tstr = re.split('[ .,!?:;"\']+', "asshole: you are, me are, shit is! this!! kurva   asf")
    #
    # # " |,|.|!|\?|:|;|\"|'"
    #
    # for token in tstr:
    #     print("Token: [" + token + ']')

    # def lazygen():
    #     for i in [[1, 2, 3], [4, 5, 6], ['a', 'b', 'c']]:
    #         for j in i:
    #             yield j
    #
    # lazy = lazygen()
    #
    # for i in range(9):
    #     print(lazy.__next__())

    arrayDictionary = simplestArrayDictionary.SimplestArrayDictionary()
    try:
        li = textFileSimplestTokenizer.TestFileSimplestTokenizer("Data/lorem_ipsum_short.txt")
        for word in li.token_generator:
            arrayDictionary.add_word(word)
        print(arrayDictionary.__str__())
    except FileNotFoundError:
        print("File not opened")

    print("End of test")


if __name__ == "__main__":
    main()
