text = input()
biggest_current_len = 1
current_len = 1
if ' ' in text:
    for i in range(len(text) - 1):
        if text[i] == text[i + 1] and text[i] == ' ':
            current_len += 1
            biggest_current_len = max(biggest_current_len, current_len)
        else:
            current_len = 1
    print(biggest_current_len)
else:
    print(0)