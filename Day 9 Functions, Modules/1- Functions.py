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
