n = int(input())
dictionary = {}
for i in range(n):
    pair = input().split()
    rus = pair[0]
    eng = pair[1]
    dictionary[rus] = eng
phrase = input()
words = phrase.split()
translated = []
for word in words:
    if word in dictionary:
        translated.append(dictionary[word])
    else:
        translated.append(word)
result = ' '.join(translated)
print(result)