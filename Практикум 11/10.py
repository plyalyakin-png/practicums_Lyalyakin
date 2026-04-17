lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

start, end = map(int, input().split())

elements = lst1[start-1:end]
lst2.extend(elements[::-1])
lst1 = lst1[:start-1] + lst1[end:]

print(lst1)
print(lst2)