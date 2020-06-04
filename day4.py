#using hashmap
def find_unique_word1(words):
    unique_counter = {}
    for i in range(len(words)):
        unique_counter[words[i]] = 0
    for i in range(len(words)):
        if words[i] in unique_counter.keys():
            unique_counter[words[i]] += 1 
    for i in range(len(words)):
        if unique_counter[words[i]] == 1:
            return i
    return -1


def find_unique_word2(words):
    for i in range(len(words)):
        if not (words[i] in words[i+1:]) and not (words[i] in words[:i]):
            return i
    return -1

print(find_unique_word1("example"))
print(find_unique_word2("example"))