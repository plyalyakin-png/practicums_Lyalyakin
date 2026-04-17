def counter(line):
    """
    Receives text and returns the number of vowels and consonantsю
    """
    count_vowel = 0
    count_consonant = 0

    for char in line.lower():
        if char in 'уеыаоэяиюё':
            count_vowel += 1

        if char in 'бвгджзйклмнпрстфхчцшщ':
            count_consonant += 1

    print(count_vowel)
    print(count_consonant)
line = input()
counter(line)