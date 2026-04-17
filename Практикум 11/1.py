numbers = []
for i in range(10):
    num = int(input())
    numbers.append(num)
new_numbers = []
for i in range(1, 9):
    sum_neighbors = numbers[i - 1] + numbers[i + 1]
    new_numbers.append(sum_neighbors)
print(new_numbers)