sweet = set(input().split())
n = int(input())
friends = set()
for i in range(n):
    friends.update(input().split())
only_sweet = sweet.difference(friends)
print(len(only_sweet))