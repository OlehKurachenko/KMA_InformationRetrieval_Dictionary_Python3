from src.indexes.incidence_matrix import IncidenceMatrix
import glob

def main():
    a = list(glob.glob("DicData/*/*"))
    im = IncidenceMatrix(a)
    im.export("data/im2.txt")


if __name__ == "__main__":
    main()
