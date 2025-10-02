def count_words(path_to_file):
    with open(path_to_file) as f:
        count = f.read().split().__len__()
        print(f"Found {count} total words")


def count_letters(path_to_file):
    with open(path_to_file) as f:
        words = f.read().split()
        counters = dict()
        for word in words:
            for i in range(0,len(word)):
                if word[i].lower() in counters:
                    counters[word[i].lower()] +=1
                else:
                    counters[word[i].lower()] = 1
        print(counters)