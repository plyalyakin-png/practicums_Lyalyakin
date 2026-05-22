text = input()
words = text.split()
dictionary = {}
for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
sorted_words = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(word)