words = input().split()
count_hole = 0
count_not_hole = 0
words_with_two_more_holes = []
hole_symbols = ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q']
for word in words:
    holes_in_words = 0
    for letter in word:
        if letter in hole_symbols:
            holes_in_words += 1
            count_hole += 1
        else:
            count_not_hole += 1
    if holes_in_words >= 2:
        words_with_two_more_holes.append(word)
print(count_hole)
print(count_not_hole)
print(words_with_two_more_holes)
