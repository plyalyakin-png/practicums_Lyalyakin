try:
    try:
        with open('input.txt', 'r', encoding='utf-8') as input:
            lines = input.readlines()
            quantity = int(lines[0])

            with open('output.txt', 'w', encoding='utf-8') as output:
                if len(lines) == quantity + 1:
                    output.write('YES')
                else:
                    output.write('NO')
    except ValueError:
        with open('output.txt', 'w', encoding='utf-8') as output:
            output.write('ERROR')

except FileNotFoundError:
    print('A file with this name was not found.')




