# Web scraping is the process of extracting and collecting data from websites and storing it on a
# local machine or in a database.

import requests
from bs4 import BeautifulSoup  # Beautiful Soup is a library that makes it easy to scrape information

# from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating,
# searching, and modifying the parse tree.

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'templates.parser')

print(response)
# print(content)
# print(soup)
print(soup.title)
print(soup.title.get_text())

tables = soup.find_all('table', {'cellpadding': '3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0]  # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)
