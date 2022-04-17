# * for tuples
# ** for Lists

def sum_number(a, b, c, d):
    return a + b + c + d


nmb = [1, 2, 3, 4]
# print(sum_number(nmb)) # TypeError
print(sum_number(*nmb))

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers))  # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)  # [2, 3, 4, 5,6]

# A list or a tuple can also be unpacked like this:


countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)  # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)  # 1 [2, 3, 4, 5, 6] 7


# Unpacking Dictionaries

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'


dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
print(unpacking_person_info(**dct))  # Asabeneh lives in Finland, Helsinki. He is 250 years old.


# Packing arguments

def sum_numbers(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


summed = sum_numbers(12, 3, 0, 2, 3, 1, 32, 1, 32, 4, 124, 12, 4, 51, 2)
print(summed)


# Packing Dictionaries

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs


print(packing_person_info(name="Asabeneh",
                          country="Finland", city="Helsinki", age=250))

# Spreading in Python

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_one]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# Creating enumerate objects

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:", type(obj1))  # Return type: <class 'enumerate'>
print(list(enumerate(l1)))  # [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

# changing start index to 2 from 0
print(list(enumerate(s1, 2)))  # [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

# Zipping

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit': f, 'veg': v})

print(fruits_and_veges)
