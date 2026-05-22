n = int(input())
antonyms = {}
for i in range(n):
    pair = input().split()
    word1 = pair[0]
    word2 = pair[1]
    antonyms[word1] = word2
    antonyms[word2] = word1
word = input()
if word in antonyms:
    print(antonyms[word])
else:
    print(word)