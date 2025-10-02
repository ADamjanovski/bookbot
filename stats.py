def count_words(path_to_file):
    with open(path_to_file) as f:
        count = f.read().split().__len__()
        print(f"Found {count} total words")

def sort_on(items):
    return items["num"]


def rearange(path_to_file):
    with open(path_to_file) as f:
        words = f.read().split()
        counters = dict()
        for word in words:
            for i in range(0,len(word)):
                if word[i].lower() in counters:
                    counters[word[i].lower()] +=1
                else:
                    counters[word[i].lower()] = 1    
        new_dic=list()
        for key in counters:
            new_dic.append({"char" : key,"num": counters[key]})

        new_dic.sort(reverse=True, key=sort_on)
        for item in new_dic:
            print(f"{item['char']}: {item['num']}")
    

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