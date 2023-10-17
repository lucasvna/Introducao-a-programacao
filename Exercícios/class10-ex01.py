#  Develop a program to write a 20 position vector Q (only positive numbers). Write:

    #The value of the highest element of Q and the position it occupies in the vector;
    #The value of the lowest element of Q and the position it occupies in the vector;
    
from random import randint

q = []

for number in range(20):
    q.append(randint(1, 100))

print(q)

highest = -1
lower = 101

for i in q:
    if highest < i:
        highest = i

    if lower > i:
        lower = i

print(f'The highest value is {highest}.\nThe lower value is {lower}.')


#All that 'for i in q blablabla' can be reduced using the code below:
print(max(q))
print(min(q))