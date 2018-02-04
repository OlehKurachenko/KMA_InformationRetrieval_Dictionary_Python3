from src.indexes.incidence_matrix import IncidenceMatrix
from src.indexes.inverted_index import InvertedIndex
from src.two_words_index.two_words_inverted_index import TwoWordsInvertedIndex
import glob

def practice2():
    a = list(glob.glob("DicData/Samples/*"))
    im = IncidenceMatrix(a)
    im.export("data/im2.txt")

    ii = InvertedIndex(a)
    ii.export("data/ii.txt")

    print(ii.perform_request("d or ( a and c )"))

def practice3():
    a = list(glob.glob("DicData/Samples/*"))
    twii = TwoWordsInvertedIndex(a)
    twii.export("data/twii.txt")

    print(twii.perform_request("d d"))

def main():
    practice3()


if __name__ == "__main__":
    main()
