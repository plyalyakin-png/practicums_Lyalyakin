def convert_datetime(datetime_str):
    """
    Convert datetime from 'MM/DD/YYYY HR:MIN:SEC' format to 'DD.MM.YY HR:MIN:SEC AM/PM' format.
    """
    try:
        parts = datetime_str.split(' ')
        if len(parts) != 2:
            print("Invalid format")
            return

        date_part, time_part = parts

        date_components = date_part.split('/')
        if len(date_components) != 3:
            print("Invalid format")
            return

        month, day, year = date_components

        time_components = time_part.split(':')
        if len(time_components) != 3:
            print("Invalid format")
            return

        hour, minute, second = time_components

        month = int(month)
        day = int(day)
        year = int(year)
        hour = int(hour)
        minute = int(minute)
        second = int(second)

        if month < 1 or month > 12:
            print("Invalid month")
            return

        if day < 1 or day > 31:
            print("Invalid day")
            return

        if hour < 0 or hour > 23:
            print("Invalid hour")
            return

        if minute < 0 or minute > 59:
            print("Invalid minute")
            return

        if second < 0 or second > 59:
            print("Invalid second")
            return

        if hour == 0:
            hour_12 = 12
            period = "AM"
        elif hour < 12:
            hour_12 = hour
            period = "AM"
        elif hour == 12:
            hour_12 = 12
            period = "PM"
        else:
            hour_12 = hour - 12
            period = "PM"

        year_short = year % 100

        result = f"{day:02d}.{month:02d}.{year_short:02d} {hour_12}:{minute:02d}:{second:02d} {period}"
        print(result)

    except ValueError:
        print("Invalid format")
        return


convert_datetime("12/25/2023 14:30:45")
convert_datetime("01/01/2000 00:00:00")
convert_datetime("122/04/1990 13:12:12")
convert_datetime("06/15/1985 12:00:00")
convert_datetime("03/20/2024 23:59:59")