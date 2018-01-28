from src.indexes.incidence_matrix import IncidenceMatrix
from src.indexes.inverted_index import InvertedIndex
import glob


def main():
    a = list(glob.glob("DicData/Samples/*"))
    im = IncidenceMatrix(a)
    im.export("data/im2.txt")

    ii = InvertedIndex(a)
    ii.export("data/ii.txt")

    print(ii.perform_request("d or ( a and c )"))


if __name__ == "__main__":
    main()
