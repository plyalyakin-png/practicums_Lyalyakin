nums = list(map(int, input().split()))
num = int(input())
if nums.count(num) > 1:
    print("YES")
else:
    print("NO")