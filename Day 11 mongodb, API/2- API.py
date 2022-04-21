import os

from flask import Flask, Response, request
from bson.objectid import ObjectId
from bson.json_util import dumps
from datetime import datetime
import pymongo
import json

from dotenv import dotenv_values

config = dotenv_values("../.env")
MONGODB_URI = config['MONGODB_PATH']

client = pymongo.MongoClient(MONGODB_URI)
app = Flask(__name__)

db = client.school


@app.route('/api/v1.0/students-local', methods=['GET'])
def students_local():
    student_list = [
        {
            'name': 'Asabeneh',
            'country': 'Finland',
            'city': 'Helsinki',
            'skills': ['HTML', 'CSS', 'JavaScript', 'Python']
        },
        {
            'name': 'David',
            'country': 'UK',
            'city': 'London',
            'skills': ['Python', 'MongoDB']
        },
        {
            'name': 'John',
            'country': 'Sweden',
            'city': 'Stockholm',
            'skills': ['Java', 'C#']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')


@app.route('/api/v1.0/test', methods=['GET'])
def test():
    # db = client.school
    # db.students.insert_one({'name': 'Asabeneh',
    #                         'country': 'Finland',
    #                         'city': 'Helsinki',
    #                         'skills': ['HTML', 'CSS', 'JavaScript', 'Python']})
    return Response(client.list_database_names())


@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    student = db.students.find({'_id': ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')


@app.route('/api/v1.0/students', methods=['GET'])
def students():
    student = db.students.find()
    return Response(dumps(student), mimetype='application/json')


@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    # request.json['name']: use indexing if you know the key exists
    # request.json.get('name'): use get if the key might not exist, if not exist value will be null on db
    # request.args.get('sad')

    name = request.json.get('name')
    country = request.json.get('country')
    city = request.json.get('city')
    skills = request.json.get('skills').split(', ')
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'skills': skills,
        'created_at': created_at
    }
    db.students.insert_one(student)
    return Response(dumps({"result": "a new student has been created"}), status=201, mimetype='application/json')


@app.route('/api/v1.0/students/<id>', methods=['PUT'])  # this decorator create the home route
def update_student(id):
    query = {"_id": ObjectId(id)}
    name = request.json.get('name')
    country = request.json.get('country')
    city = request.json.get('city')
    skills = request.json.get('skills').split(', ')
    updated_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'skills': skills,
        'updated_at': updated_at
    }
    db.students.replace_one(query, student)
    return Response(dumps({"result": "a new student has been updated"}), mimetype='application/json')


@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    db.students.delete_one({"_id": ObjectId(id)})
    return Response(dumps({"result": "successfully deleted"}), mimetype='application/json')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
