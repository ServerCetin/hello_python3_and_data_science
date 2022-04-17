# open('file_name', mode)

# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

#The default mode of open is reading, so we do not have to specify 'r' or 'rt'.

with open('hello_file.txt','w') as file: # when we use with 'with' file closes itself otherwise we should close it ourselves
    file.write('This is a message to hello file!')

f = open('hello_file.txt')
txt = f.read()
# txt = f.read(10) # only 10 char
line = f.readline() # only first line
lines = f.readlines() # readlines(): read all the text line by line and returns a list of lines
lines = f.read().splitlines() # same as above

print(type(txt)) # <class 'str'>
print(txt) # This is a message to hello file!
f.close()


#Deleting Files

import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')


# Changing JSON to Dictionary

import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# Changing Dictionary to JSON

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

# Saving as JSON File

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)


# File with csv Extension

import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

# File with xlsx Extension

import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)

# Python XML https://docs.python.org/2/library/xml.etree.elementtree.html