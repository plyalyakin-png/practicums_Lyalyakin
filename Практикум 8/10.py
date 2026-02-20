sentence = input().lower().split()
first_word = sentence[0]
for i in range(1, len(sentence)):
    word = sentence[i]
    if word != first_word:
        for letter in word:
            if letter.isalpha() and word.count(letter) > 1:
                break
        else:
            print(word)





