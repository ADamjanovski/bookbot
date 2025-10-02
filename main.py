import sys
def read_book(path_to_file):
    with open(path_to_file) as f:
        print(f.read())

def count_words(path_to_file):
    with open(path_to_file) as f:
        count = f.read().split().__len__()
        print(f"Found {count} total words")


if __name__ == "__main__":
    args = sys.argv
    count_words("./books/frankenstein.txt")