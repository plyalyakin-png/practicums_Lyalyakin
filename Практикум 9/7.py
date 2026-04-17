try:
    with open('input_files/input7.txt', 'r', encoding='utf-8') as input:
        lines = input.readlines()

        for line in lines:
            int_line = int(line)

            with open('output.txt', 'a', encoding='utf-8') as output:
                if int_line!=100:
                    output.write(line)
except FileNotFoundError:
    print('A file with this name was not found.')