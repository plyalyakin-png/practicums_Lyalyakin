import itertools

input_string = input()
numbers_as_strings = input_string.split()
unique_numbers = set(map(int, numbers_as_strings))
sorted_elements = sorted(unique_numbers)

all_subsets = []
total_elements = len(sorted_elements)

for subset_size in range(total_elements + 1):
    combinations_generator = itertools.combinations(sorted_elements, subset_size)
    for current_combination in combinations_generator:
        current_subset = list(current_combination)
        all_subsets.append(current_subset)
print(all_subsets)