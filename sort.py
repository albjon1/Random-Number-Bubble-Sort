import time
import random

# Starting runtime
start_time = time.time()


# Bubble Sort Function / Time Complexity - O(n^2)
def id_sort(array):
    swap = True
    while swap:
        swap = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True


# Creating randomly generated list of 1000 integers
random_list = []

for i in range(1000):
    nums = random.randint(1, 100000)
    random_list.append(nums)

print('Generated list = ', random_list)
id_sort(random_list)  # Running algorithm on the list
print('Sorted = ', random_list)

# Ending Runtime
end_time = time.time()

print('''
''')

# Runtime is displayed
print(f"Runtime = {end_time - start_time}")
