def sorter(string):
    sorted_symbols = sorted(list(string))
    sorted_string = ''.join(sorted_symbols)
    print(sorted_string)
string = input()
sorter(string)