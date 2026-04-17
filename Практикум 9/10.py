try:
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    current_date_str = lines[0].strip()
    current_parts = current_date_str.split('.')
    current_day = int(current_parts[0])
    current_month = int(current_parts[1])

    current_day_of_year = current_day
    for i in range(current_month - 1):
        current_day_of_year += months[i]

    n = int(lines[1].strip())

    with open('output.txt', 'w', encoding='utf-8') as output_file:
        for i in range(2, 2 + n):
            line = lines[i].strip()
            parts = line.split()

            cell_number = parts[0]
            storage_date_str = parts[1]

            storage_parts = storage_date_str.split('.')
            storage_day = int(storage_parts[0])
            storage_month = int(storage_parts[1])

            storage_day_of_year = storage_day
            for j in range(storage_month - 1):
                storage_day_of_year += months[j]

            if current_day_of_year - storage_day_of_year > 3:
                output_file.write(cell_number + '\n')

except FileNotFoundError:
    print('A file with this name was not found.')