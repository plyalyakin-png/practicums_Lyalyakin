cities = input().replace('ь', '').replace('ъ', '').replace('ы','')
words = cities.lower().split()
for i in range(len(words)-1):
    if words[i + 1][0] != words[i][-1]:
        if (i + 1) % 2 == 0:
            print('Вася')
        else:
            print('Петя')
        break
else:
    if (len(words) - 1) % 2 == 0:
        print('Петя')
    else:
        print('Вася')