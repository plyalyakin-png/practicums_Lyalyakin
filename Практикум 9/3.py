try:
    with open('input3.txt', 'r', encoding='utf-8') as input:
        lines = input.readlines()

        for line in lines:
            first_symb = line[0]

            with open('output.txt', 'a', encoding='utf-8') as output:
                output.write(first_symb)

except FileNotFoundError:
    print('A file with this name was not found.')