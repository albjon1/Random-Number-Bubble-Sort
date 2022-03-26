import time
import random

# Starting runtime
start_time = time.time()


# Bubble Sort Function
def b_array(array):
    swap = True
    while swap:
        swap = False
        for x in range(len(array) - 1):
            if array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]
                swap = True


# Creating randomly generated list of 1000 integers
random_list = []

for i in range(1, 1001):
    nums = random.randint(1, 100001)
    random_list.append(nums)

print('Generated list = ', random_list)
b_array(random_list)  # Running the algorithm on the list
print('sorted = ', random_list)

# Ending Runtime
end_time = time.time()

print('''
''')

# Runtime is displayed
print(f"Runtime = {end_time - start_time}")
