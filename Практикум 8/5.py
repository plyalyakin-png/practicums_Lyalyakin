string_1 = input()
string_2 = input()
string_3 = input()
unique_symbols = []
for i in range(len(string_1)):
    if string_1[i] not in string_2 and string_1[i] not in string_3:
        unique_symbols.append(string_1[i])
for i in range(len(string_2)):
    if string_2[i] not in string_3 and string_2[i] not in string_1:
         unique_symbols.append(string_2[i])
for i in range(len(string_3)):
    if string_3[i] not in string_1 and string_3[i] not in string_2:
         unique_symbols.append(string_3[i])
print(','.join(unique_symbols))
