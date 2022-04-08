# There are four collection data types in Python :(https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md)

# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
# Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
# Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set.
#       Duplicate members are not allowed.
# Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

empty_list = list()
empty_list2 = []

print(len(empty_list))  # 0

cities_of_turkey = ["İstanbul", "Ankara", "İzmir", "Ordu", "and the other 77"]
complex_list = ['Server', 'Çetin', 87, {'facebook': 'f.co/sc', 'twitter': "tw/sc"}]

print(complex_list[3]['facebook'])  # f.co/sc

# unpacking
lst = ['item', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)  # item1
print(second_item)  # item2
print(third_item)  # item3
print(rest)  # ['item4', 'item5']

# unpacking
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# getting child
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[1] = 'avocado'

# does exist
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# adding an item: To add item to the end of an existing list we use the method append().
item = "new_item"
lst = list()
lst.append(item)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')  # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)

# Inserting Items into a List:
# We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to
# the right. The insert() methods takes two arguments:index and an item to insert.

# syntax
index = 2
lst = ['item1', 'item2']
lst.insert(index, item)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')  # insert apple between orange and mango
print(fruits)  # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')  # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

# Removing Items from a List

# syntax
lst = ['item1', 'item2']
lst.remove('item1')

# Removing Items Using Pop
# The pop() method removes the specified index, (or the last item if index is not specified):

lst = ['item1', 'item2']
lst.pop()  # last item
lst.pop(0)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)  # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)  # ['orange', 'mango']

# Clearing List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)  # []

# copy
lst = ['item1', 'item2']
lst_copy = lst.copy()

# Joining Lists
# list3 = list1 + list2
# or
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)

# Counting Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))  # 3

# Sorting List Items
lst = ['item1', 'item2']
lst.sort()  # ascending
lst.sort(reverse=True)  # descending

# sorted(): returns the ordered list without modifying the original list Example:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
