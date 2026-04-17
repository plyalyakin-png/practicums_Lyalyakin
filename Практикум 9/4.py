try:
    with open('input4.txt', 'r', encoding='utf-8') as input:
        lines = input.readlines()

        for line in lines:
            if len(line.rstrip('\n')) > 20:

                with open('output.txt', 'a', encoding='utf-8') as output:
                    output.write(line)
except FileNotFoundError:
    print('A file with this name was not found.')