number = input().strip()
print('\n' * 25)
for tries in range(10):
    bulls = 0
    cows = 0
    move = input().strip()
    for i in range(len(move)):
        if move[i] == number[i]:
            bulls += 1
    for i in range(len(move)):
        if move[i] != number[i]:
            for j in range(len(move)):
                if move[j] == number[i]:
                    cows += 1
                    break
    print(f'Быков:{bulls} Коров:{cows}')
    if bulls == 4:
        print('Победа')
        break
else:
    print('Поражение')
