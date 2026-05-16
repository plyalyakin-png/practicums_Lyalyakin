import itertools

raw_input = input().split()
unique_numbers = set(map(int, raw_input))
sorted_elements = sorted(unique_numbers)

k = int(input())

k_subsets = []
combinations_iterator = itertools.combinations(sorted_elements, k)

for combination_tuple in combinations_iterator:
    subset_list = list(combination_tuple)
    k_subsets.append(subset_list)
print(k_subsets)