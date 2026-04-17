all_words = []
while True:
    line = input()
    if line == '':
        break

    for word in line.split():
        word_lower = word.lower()

        clean_chars = []
        for char in word_lower:
            if char.isalpha() or char.isdigit():
                clean_chars.append(char)

        clean_word = ''.join(clean_chars)

        if clean_word:
            all_words.append(clean_word)

freq = {}
for word in all_words:
    freq[word] = freq.get(word, 0) + 1

unique_words = []
seen = set()
for word in all_words:
    if word not in seen:
        unique_words.append(word)
        seen.add(word)

sorted_words = sorted(unique_words, key=lambda w: -freq[w])

for word in sorted_words:
    print(word)