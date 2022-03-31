# where is day 2? well, I overslept. After I woke up, I went to Data event and came home late.
# so I could not study python :(

print("Hello \t tabbed \t line")

number = 1
text = "one"
float_number = 1.131241241

print("Let's print 'em all \n %d for decimal, \n %s for string, \n %.3f for float" %(number, text, float_number))

a = 1
b = 2
c = a + b

formatted_str = "{} + {} = {}".format(a,b,(a+b))
print(formatted_str),
print(f'{a} + {b} = {a + b}')

index_count_of_text = len(text) - 1
last_index_of_text = text[-1]

long_text = "this is reaaaly long text!"
first_three_char = long_text[0:3]
last_three_char = long_text[-3:]

except_first_three_char = long_text[3:]
except_last_three_char = long_text[-3:]

reversed_long_text = long_text[::-1]
skipped_slice_long_text = long_text[1:10:2] # output: 'hsi e'

# String methods
# capitalize(): Converts the first character of the string to capital letter
# count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting
#          indexing for counting and end is the last index to count.
# endswith(): Checks if a string ends with a specified ending
# find(): Returns the index of the first occurrence of a substring, if not found returns -1
# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
# format(): formats string into a nicer output (more: https://www.programiz.com/python-programming/methods/string/format)
# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0
#          and string length - 1). If the substring is not found it raises a valueError.
# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending
#           index (default 0 and string length - 1)
# isalnum(): Checks alphanumeric character
# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
# isdecimal(): Checks if all characters in a string are decimal (0-9)
# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
# islower(): Checks if all alphabet characters in the string are lowercase
# isupper(): Checks if all alphabet characters in the string are uppercase
# join(): Returns a concatenated string
# strip(): Removes all given characters starting from the beginning and end of the string
# replace(): Replaces substring with a given string
# split(): Splits the string, using given string or space as a separator
# title(): Returns a title cased string
# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
# startswith(): Checks if String Starts with the Specified String

capitalized_long_text = long_text.capitalize()
print(capitalized_long_text.count('e')) # 2
print(capitalized_long_text.count('e', 7, 14)) # 1,
print(capitalized_long_text.count('Th')) # 1

print(capitalized_long_text.endswith('xt!'))   # True
print(capitalized_long_text.endswith('tion')) # False

find_first_i_letter_index = long_text.find('i')
find_last_i_letter_index = long_text.rfind('i')

lonely_strings = ["Ali", "Veli", "49", "50"]
happy_strings = " ".join(lonely_strings) # 'Ali Veli 49 50'
