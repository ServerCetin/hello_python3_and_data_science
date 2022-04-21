# MongoDB is a NoSQL database. MongoDB stores data in a JSON like document which make MongoDB very
# flexible and scalable. Let us see the different terminologies of SQL and NoSQL databases. The
# following table will make the difference between SQL versus NoSQL databases.

# pip install pymongo dnspython

import pymongo
from bson import ObjectId
from dotenv import dotenv_values

config = dotenv_values("../.env")

MONGODB_URI = config['MONGODB_PATH']

client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

# Creating a database and collection

db = client.teams  # we can create a database like this or the second way
# db2 = client['name_of_database']

#db.football.insert_one({'name': 'Fenerbahce', 'country': 'Turkey', 'since': 1907})

print(client.list_database_names())  # ['thirty_days_of_python', 'admin', 'local']
# we created teams db and added football collection and added a football team Fenerbahce as document


# Inserting many documents to collection
# The insert_one() method inserts one item at a time if we want to insert many documents at once either
# we use insert_many() method or for loop. We can use for loop to inset many documents at once.

# students = [
#         {'name':'David','country':'UK','city':'London','age':34},
#         {'name':'John','country':'Sweden','city':'Stockholm','age':28},
#         {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
#     ]
# for student in students:
#     db.students.insert_one(student)


# MongoDB Find
# The find() and findOne() methods are common method to find data in a collection in mongoDB database.
# It is similar to the SELECT statement in a MySQL database. Let us use the find_one() method to
# get a document in a database collection.

t = db.football.find_one() # '_id': ObjectId('625f5581c19b8c217b7d532b'), 'name': 'Fenerbahce', 'country': 'Turkey', 'since': 1907}
t2 = db.football.find_one({'_id': ObjectId('625f5581c19b8c217b7d532b')})
all_teams = db.football.find()
all_teams_filtered = db.football.find({}, {"_id":0,  "name": 1, "country":1}) # 0 means not include and 1 means include
print(t)
print(t2)

for team in all_teams:
    print(team) # {'_id': ObjectId('625f5774e3110dc726b381ae'), 'name': 'Fenerbahce', 'country': 'Turkey', 'since': 1907} ...

for team in all_teams_filtered:
    print(team) # {'name': 'Fenerbahce', 'country': 'Turkey'} ...

# Find with Query

query = {
    'country': 'Turkey'
}

all_teams_with_query = db.football.find(query)

for team in all_teams_with_query:
    print(team) # {'_id': ObjectId('625f5774e3110dc726b381ae'), 'name': 'Fenerbahce', 'country': 'Turkey', 'since': 1907}

# Limiting documents
# db.football.find().limit(5)

# Find with sort
# db.football.find().sort('name')
# db.students.find().sort('name',-1)


#Updating with query
query = {'name':'Fenerbahce'}
new_value = {'$set' : {'name' : 'FB'}}

db.football.update_one(query, new_value)
# lets check the result if the age is modified
for team in db.football.find():
    print(team)

# DELETING WITH QUERY
query = {'name':'FB'}
db.football.delete_one(query)

# Drop a collection : Using the drop() method we can delete a collection from a database.
db.football.drop()

for team in db.football.find():
    print(team)
