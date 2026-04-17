try:
    with open('input2.txt', 'r', encoding='utf-8') as input:
        lines = input.readlines()
        for line in lines:
            if line[0]=='a' or line[0]=='A':
                with open('output.txt', 'a', encoding='utf-8') as output:
                    output.write(line)
                continue
except FileNotFoundError:
    print('A file with this name was not found.')

