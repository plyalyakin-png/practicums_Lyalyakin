text = input()
counter = 0
for symbol in text:
    if symbol == '(':
        counter += 1
    elif symbol == ')':
        counter -= 1
        if counter < 0:
            break
if counter == 0:
    print('Correct')
else:
    print('Incorrect')