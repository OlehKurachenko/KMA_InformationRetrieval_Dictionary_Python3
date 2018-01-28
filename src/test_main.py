from src.indexes.incidence_matrix import IncidenceMatrix
from src.indexes.inverted_index import InvertedIndex
import glob


def main():
    a = list(glob.glob("DicData/Samples/*"))
    im = IncidenceMatrix(a)
    im.export("data/im2.txt")

    ii = InvertedIndex(a)
    ii.export("data/ii.txt")


if __name__ == "__main__":
    main()
