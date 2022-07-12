def void_function():
    print("Hello functions!")


void_function()


def two_num_sums(nmb1, nmb2):
    return nmb1 + nmb2;


print(two_num_sums(1, 2))


# Passing Arguments with Key and Value
# If we pass the arguments with key and value, the order of the arguments does not matter.

def print_my_fullname(firstname, lastname):
    print(firstname + " " + lastname)


print_my_fullname(lastname="ÇETİN", firstname="Server")


# If we do not return a value with a function, then our function is returning None by default

def print_something(text="default text"):
    print(text)


print_something()


# Arbitrary Number of Arguments
# If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary
# number of arguments by adding * before the parameter name.

def print_max_number(*args):
    print(max(args))


# Calling function

print_max_number(1, 3, 1, 5, 6, 12, 8)


def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)


print(generate_groups('Team-1', 'Asabeneh', 'Brook', 'David', 'Eyob'))


# You can pass functions around as parameters
def square_number(n):
    return n * n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))  # 27


def square_generator(list):  # generators not returns all values immediately, we need to ask it to generate value
    for num in list:
        yield (num * num)


list = [1, 2, 3, 4, 5, 6]
gen = square_generator(list)
print(gen)  # <generator object square_generator at 0x0000020952A346D0>
print(next(gen))  # 1
print(next(gen))  # 4
print(next(gen))  # 9
print(next(gen))  # 16
print(next(gen))  # 25
print(next(gen))  # 36
# print(next(gen))  # Exhaust:      Traceback (most recent call last): StopIteration


# list comprehension and generator
l = [x * x for x in [1, 2, 3, 4, 5, 6]]  # [1, 4, 9, 16, 25, 36]
print(l)

g = (x * x for x in [1, 2, 3, 4, 5, 6])  # [1, 4, 9, 16, 25, 36]
print(next(g))  # 1

# similar to range function
def range_generator(start, end, step):
    current = start

    while current < end:
        yield current
        current += step

r = range_generator(1,20,3)
print(next(r)) # 1
print(next(r)) # 4
print(next(r)) # 7

