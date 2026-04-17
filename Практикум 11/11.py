result = list(map(int, input().split()))
command = input()

direction = command[0]
shift = int(command[1:])

shift = shift % len(result)

if direction == 'R':
    result = result[-shift:] + result[:-shift]
elif direction == 'L':
    result = result[shift:] + result[:shift]
print(result)