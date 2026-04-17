numbers = input().split()
summ_odd = 0
summ_even = 0
for i in range(len(numbers)):
    num = int(numbers[i])
    if num % 2 == 0:
        summ_even += num
    else:
        summ_odd += num
print(summ_even)
print(summ_odd)
