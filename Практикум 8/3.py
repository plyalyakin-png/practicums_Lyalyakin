text = input().lower()
result = 0
for i in range(len(text)):
    new_text = text[:i:1]
    if text[i] not in new_text and text[i].isalpha():
        result += 1
print(result)