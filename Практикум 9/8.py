try:
    with open('input.txt', 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    steps = []
    for line in lines:
        int_line = int(line.strip())
        steps.append(int_line)
    if len(steps) == 366:
        days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    with open('output.txt', 'w', encoding='utf-8') as output_file:
        current_day = 0
        for days_in_month in days_in_months:
            month_steps = 0
            for i in range(days_in_month):
                month_steps += steps[current_day]
                current_day += 1
            avg_steps = month_steps / days_in_month
            output_file.write(f"{avg_steps}\n")
except FileNotFoundError:
    print('A file with this name was not found.')