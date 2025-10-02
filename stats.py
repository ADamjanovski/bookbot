def count_words(path_to_file):
    with open(path_to_file) as f:
        count = f.read().split().__len__()
        print(f"Found {count} total words")
