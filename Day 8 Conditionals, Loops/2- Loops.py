nmbr = 0;

while nmbr != 5:
    print(nmbr)
    nmbr += 1
else:
    print(nmbr)

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in number_list:
    print(number)

# String for

str = "Interesting"

for i in range(len(str)):
    print(str[i])

# Tuple print

tpl = ("1", 2, False, 52)
for item in tpl:
    print(item)

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
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)  # this way we get both keys and values printed out

for number in range(11):
    print(number)  # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# In python when statement is required (after semicolon), but we don't like to execute any code there,
# we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
for number in range(6):
    pass
