n = int(input())
dictionary = {}
for i in range(n):
    parts = input().split()
    form = parts[0]
    items = parts[1:]
    for item in items:
        dictionary[item] = form
word = input()
print(dictionary[word])