import time
import random

# Starting runtime
start_time = time.time()


# Bubble array Function
def b_array(array):
    swap = True
    while swap:
        swap = False
        for x in range(len(array) - 1):
            if array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]
                swap = True


# Creating randomly generated list of 1000 integers
randomList = []

for i in range(1, 1001):
    nums = random.randint(1, 100001)
    randomList.append(nums)

print('Generated list = ', randomList)
b_array(randomList)  # Running the algorithm on the list
print('sorted = ', randomList)

# Ending Runtime
end_time = time.time()

print('''
''')

# Runtime is displayed
print(f"Runtime = {end_time - start_time}")
