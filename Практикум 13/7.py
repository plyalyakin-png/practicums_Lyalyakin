import itertools
nums = sorted(input().split())
for i in itertools.permutations(nums):
    print(' '.join(i))