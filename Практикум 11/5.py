line = input()
numbers = []
for i in line.split():
    numbers.append(int(i))

total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(average)