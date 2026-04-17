nums = []
line = input()
for i in line.split():
    nums.append(int(i))

new_nums = []
for num in nums:
    if num != 3:
        new_nums.append(num)
print(new_nums)