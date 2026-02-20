sentence = input().split()
sentence.sort(key=len)
print(' '.join(sentence))