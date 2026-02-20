text = input()
for i in range(len(text)):
    if text.count(text[i]) == 3:
        print(text[i])
        break