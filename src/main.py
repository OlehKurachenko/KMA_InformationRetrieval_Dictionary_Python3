from src import textFileSimplestTokenizer, simplestArrayDictionary


def main():
    array_dictionary = simplestArrayDictionary.SimplestArrayDictionary()
    try:
        li = textFileSimplestTokenizer.TestFileSimplestTokenizer("Data/lorem_ipsum.txt")
        for word in li.token_generator:
            array_dictionary.add_word(word)
        print(array_dictionary.__str__())
        array_dictionary.export_dictionary("data/dic1.txt")
    except FileNotFoundError:
        print("File not opened")

    try:
        array_dictionary2 = simplestArrayDictionary.SimplestArrayDictionary("data/dic1.txt")
        print(array_dictionary2)
    except FileNotFoundError:
        print("Dictionary file not found")


if __name__ == "__main__":
    main()
