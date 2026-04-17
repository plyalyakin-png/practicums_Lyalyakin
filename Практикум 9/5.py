try:
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()
    try:
        first_num = int(lines[0].strip())
        second_num = int(lines[1].strip())
        third_num = int(lines[2].strip())
        try:
            result = first_num / second_num + third_num
            with open('output.txt', 'w', encoding='utf-8') as output_file:
                output_file.write(str(result))
        except ZeroDivisionError:
            print('Division by 0')
    except ValueError:
        print('Data error')
except FileNotFoundError:
    print('A file with this name was not found.')