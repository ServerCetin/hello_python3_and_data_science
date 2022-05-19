'''
    This chapter will allow you to apply all the concepts you've learned in this course. You will use hacker
    statistics to calculate your chances of winning a bet. Use random number generators, loops, and Matplotlib
    to gain a competitive edge!

    we are in the empire state building
    we will dice 100 times
    if it is 1 or 2 we will go downer floor
    if it is 3,4 or 5 we will go upper floor
    if it is 6 we throw the dice again. The number of eyes is the number of steps you go up.

    we cannot go downer 0 floor
    we have 0.1% chance to falling down the stairs: start from step 0
    we said we will reach 60 step
    what is the chance winning this bet

    1- Analytically calculating
    2- Simulate the process
        -Hacker Statistics: we will simulate this thousands of times
'''

import numpy as np
import matplotlib.pyplot as plt

random_number = np.random.randint(0, 3)  # 0,1,2
print(random_number)

#np.random.seed(123)  # when you pick a seed the random numb will be same
print(np.random.rand())


# Simulate random walk 500 times
all_walks = []
for i in range(500):
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]

# Plot histogram of ends, display plot
plt.plot(np_aw_t)
plt.show()
plt.clf()

plt.hist(ends, bins=15)
plt.show()

# the answer is ends with >60 divided 500 which is randomed states

result_chance = len(ends[ends >= 60]) / 500
print(result_chance)