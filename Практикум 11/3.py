sentence = input()
parts = sentence.split()

words = []
for part in parts:
    word = ""
    for symbol in part:
        if symbol.isalpha():
            word += symbol

    if len(word) > 0:
        words.append(word)
print(words)