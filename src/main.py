from src import text_file_simplest_tokenizer, simplest_array_dictionary, simplest_set_dictionary
import glob

def main():
    array_dictionary = simplest_array_dictionary.SimplestArrayDictionary()
    set_dictionary = simplest_set_dictionary.SimplestSetDictionary()
    try:
        for filename in glob.glob('Data/Egmont.txt'):
            fst = text_file_simplest_tokenizer.TestFileSimplestTokenizer(filename)
            for word in fst.token_generator:
                array_dictionary.add_word(word)
                set_dictionary.add_word(word)
    except FileNotFoundError:
        print("File not opened")
    array_dictionary.export_dictionary("data/arr_dic.txt")
    set_dictionary.export_dictionary("data/set_dic.txt")

    try:
        array_dictionary2 = simplest_array_dictionary.SimplestArrayDictionary("data/set_dic.txt")
        set_dictionary2 = simplest_set_dictionary.SimplestSetDictionary("data/arr_dic.txt")
        array_dictionary2.export_dictionary("data/arr_dic2.txt")
        set_dictionary2.export_dictionary("data/set_dic2.txt")
    except FileNotFoundError:
        print("Dictionary file not opened")


if __name__ == "__main__":
    main()
