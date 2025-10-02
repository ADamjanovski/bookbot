import sys
from stats import count_words , count_letters
def read_book(path_to_file):
    with open(path_to_file) as f:
        print(f.read())



if __name__ == "__main__":
    args = sys.argv
    count_letters("./books/frankenstein.txt")