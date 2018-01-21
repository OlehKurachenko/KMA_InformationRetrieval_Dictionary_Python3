from src import textFileSimplestTokenizer, simplestArrayDictionary, simplestSetDictionary
import glob

def main():
    array_dictionary = simplestArrayDictionary.SimplestArrayDictionary()
    set_dictionary = simplestSetDictionary.SimplestSetDictionary()
    try:
        for filename in glob.glob('Data/Egmont.txt'):
            fst = textFileSimplestTokenizer.TestFileSimplestTokenizer(filename)
            for word in fst.token_generator:
                array_dictionary.add_word(word)
                set_dictionary.add_word(word)
    except FileNotFoundError:
        print("File not opened")
    array_dictionary.export_dictionary("data/arr_dic.txt")
    set_dictionary.export_dictionary("data/set_dic.txt")

    try:
        array_dictionary2 = simplestArrayDictionary.SimplestArrayDictionary("data/set_dic.txt")
        set_dictionary2 = simplestSetDictionary.SimplestSetDictionary("data/arr_dic.txt")
        array_dictionary2.export_dictionary("data/arr_dic2.txt")
        set_dictionary2.export_dictionary("data/set_dic2.txt")
    except FileNotFoundError:
        print("Dictionary file not opened")


if __name__ == "__main__":
    main()
