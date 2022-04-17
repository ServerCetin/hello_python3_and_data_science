# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# Creating dictionary

dict = {}
dict2 = {"key": "value", "key2": 1}

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# print(dict2["add2"])
# Accessing an item by key name raises an error if the key does not exist.
# To avoid this error first we have to check if a key exist or we can use the get method.
# The get method returns None, which is a NoneType object data type, if the key does not exist.

print(dict2.get("add2"))
print(person.get("address"))

# Adding an item to dict
person["city"] = "X"
person['skills'].append('HTML')

# checking if item exist

print("city" in person)

# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name

# Changing Dictionary to a List of Items
print(dict2.items())  # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# Clearing a Dictionary
dict2.clear()

# Getting Dictionary Keys as a List
dict2.keys()

# Getting Dictionary Values as a List
dict2.values()

