# A module is a file containing a set of codes or a set of functions which can be included to an application. A module
# could be a file containing a single variable, a function or a big code base.

# from my_math_module import *
# from my_math_module import sums_of_two_nums
from my_math_module import sums_of_two_nums as sums  # , x as y

print(sums(1, 2))

import os

print(os.getcwd())


# Guess the Number Game
from random import random, randint

rand_num = randint(0, 99)
print("Guess, The Num It's between [0,99]")
guessed_num = -11

while (guessed_num != rand_num):
    print("Guess a number: ")
    guessed_num = int(input())

    if guessed_num == rand_num:
        print("Congrats! %d was the number!" % rand_num)
    if guessed_num < rand_num:
        print("The num is higher")
    if guessed_num > rand_num:
        print("The num is lower")
