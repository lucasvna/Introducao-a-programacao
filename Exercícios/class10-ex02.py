# From a list of numbers, create an algorithm that returns the sum of the even numbers from the list.
# Example: [1, 2, 3, 4, 5, 6]
# Result: 12

from random import randint

list = []

sum_result = 0

for n in range(20):
    list.append(randint(1, 30))

for i in list:
    if (i % 2) == 0:
        sum_result += i

print(f'The sum result is {sum_result}')
print(list)
