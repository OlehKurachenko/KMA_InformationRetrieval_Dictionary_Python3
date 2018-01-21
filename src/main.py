from src import textFileSimplestTokenizer


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

    li = textFileSimplestTokenizer.TestFileSimplestTokenizer("Data/lorem_ipsum_short.txt")
    for word in li.token_generator:
        print("Word: [" + word + ']')

    print("End of test")


if __name__ == "__main__":
    main()
