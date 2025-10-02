import sys
from stats import count_words , count_letters,rearange
def read_book(path_to_file):
    with open(path_to_file) as f:
        print(f.read())



if __name__ == "__main__":
    args = sys.argv
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
    else:
        count_words(sys.argv[1])
        rearange(sys.argv[1])


#./books/frankenstein.txt