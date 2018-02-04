from src.indexes.incidence_matrix import IncidenceMatrix
from src.indexes.inverted_index import InvertedIndex
from src.two_words_index.two_words_inverted_index import TwoWordsInvertedIndex
from src.position_indexes.positioned_index import PositionInvertedIndex
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
    pii = PositionInvertedIndex(a)
    pii.export("data/pii.txt")

    print(twii.perform_request("d d"))
    print(pii.perform_request("b d 4"))
def main():
    practice3()


if __name__ == "__main__":
    main()
