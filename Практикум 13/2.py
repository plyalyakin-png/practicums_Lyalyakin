n = int(input())
common = set(input().split())
for _ in range(n - 1):
    current = set(input().split())
    common = common.intersection(current)
print(len(common))