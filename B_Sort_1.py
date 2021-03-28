"""
Bubble sort
Author - Albjon Husha
"""
import time
import random

# Starting runtime
start_time = time.time()


def b_sort(sort):

    swap = True
    while swap:
        swap = False
        for x in range(len(sort) - 1):
            if sort[x] > sort[x + 1]:
                sort[x], sort[x + 1] = sort[x + 1], sort[x]
                swap = True


randomList = []

for i in range(0, 1000):
    nums = random.randint(0, 100000)
    randomList.append(nums)
print('Generated list = ', randomList)
b_sort(randomList)
print('Sorted = ', randomList)

# Ending Runtime
end_time = time.time()

print('''
''')

# Runtime is printed
print(f"Runtime = {end_time - start_time}")
