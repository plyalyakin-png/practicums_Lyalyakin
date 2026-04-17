import os
try:
    if not os.path.exists('simple'):
        os.mkdir('simple')

    with open('input.txt', 'r') as input:
        lines = input.readlines()

        with open('simple/output.txt', 'a') as output:
            number_line = 0
            for line in lines:
                number_line += 1

                if number_line % 2 == 0:
                    output.write(line)
except FileNotFoundError:
    print('A file with this name was not found.')