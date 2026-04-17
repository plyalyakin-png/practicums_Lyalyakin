divs = []
number = int(input())
for div in range(1, number+1):
    if number % div == 0:
        divs.append(div)
print(divs)