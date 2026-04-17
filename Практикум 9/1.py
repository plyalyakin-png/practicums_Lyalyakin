try:
    with open('input.txt', 'r', encoding='utf-8') as input:
        content = input.read().upper()
    with open('output.txt', 'w', encoding='utf-8') as output:
        output.write(content)
except FileNotFoundError:
    print('A file with this name was not found.')