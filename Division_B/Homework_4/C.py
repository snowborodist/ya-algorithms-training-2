word_dict = {}

# TODO: CHANGE THE FILENAME TO INPUT.TXT!!!
with open("input_C.txt") as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            if word in word_dict:
                word_dict[word] -= 1
            else:
                word_dict[word] = -1

for _, word in sorted([(count, word) for word, count in word_dict.items()]):
    print(word)
