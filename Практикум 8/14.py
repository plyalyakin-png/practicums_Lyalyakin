hint = input()
word = input().strip().lower()
print('\n' * 25)
print(hint)
mystery = ['*'] * len(word)
print(''.join(mystery))
tries = 10
while tries > 0:
    choice = input('Буква или слово (0 - буква, 1 - слово)?').strip()
    if choice == '0':
        letter = input().strip().lower()
        for i in range(len(word)):
            if word[i] == letter:
                mystery[i] = word[i]
        tries -= 1
        print(''.join(mystery))
        if '*' not in mystery:
            print('Победа')
            break
    elif choice == '1':
        full_word = input().strip().lower()
        if full_word == word:
            print('Победа')
            break
        else:
            print('Поражение')
            break
else:
    print('Поражение')
