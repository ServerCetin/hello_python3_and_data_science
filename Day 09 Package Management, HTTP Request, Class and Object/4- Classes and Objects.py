# Python is an object oriented programming language. Everything in Python is an object, with its
# properties and methods. A number, string, list, dictionary, tuple, set etc. used in a program is
# an object of a corresponding built-in class.

string = 'this is a string'
int_type = 1
set1 = set()
# ...

print(type(int_type))  # <class 'int'>
print(type(string))  # <class 'str'>
print(type(set1))  # <class 'set'>


# ...

# Creating a Class
# To create a class we need the key word class followed by the name and colon. Class name should be CamelCase.

# class constructor:  The init constructor function has self parameter which is a reference to the
# current instance of the class

class Human:

    def __init__(self, firstname, lastname, country, age=9):
        # self allows to attach parameter to the class
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.age = age  # this has default value

    def who_am_i(self):
        return f'I am {self.firstname} {self.lastname}. I am from {self.country}. I am {self.age} years old'


class Programmer(Human):
    instance_variable = "I am here!"
    num_programmer = 0

    def __init__(self, firstname, lastname, country, interests=[]):
        super().__init__(firstname, lastname, country)
        self.interests = interests
        Programmer.num_programmer += 1

    def add_interest(self, interest):
        self.interests.append(interest)

    def who_am_i(self):  # overriding
        age_status = 'underaged' if self.age < 18 else 'overaged'
        return f'I am {self.firstname} {self.lastname}. I am from {self.country}. I am {age_status}. ' \
               f'I am interested in {self.interests}'

    def who_was_i(self):
        return super().who_am_i()

    @classmethod
    def fake_input(cls, num):  # cls olarak class aldığımızı belli ediyoruz parametrede
        cls.num_programmer = num # Programmer.num_programmer = num

    @staticmethod
    def static_method_test(msg):
        return msg

    #  magic methods helps us to modify our classes, there are many magic methods like __add__ look at the docs
    def __str__(self):
        return f"I am Programmer(firstname:{self.firstname}, lastname:{self.lastname}, country: {self.country}) and my hobbies: {self.interests}"


server = Programmer('Server', 'ÇETİN', 'Turkey')
print(server)  # <__main__.Human object at 0x0000017C712BDFD0>
print(server.firstname)  # Server

server.add_interest('Computer Science')
server.add_interest('Data Science')
print(server.interests)
print(server.who_am_i())
print(server.who_was_i())
print(Programmer.__dict__)  # attributes
print(Programmer.instance_variable)  # attributes
print(server.fake_input(1000))
print(server.num_programmer)
print(Programmer.num_programmer)
print(Programmer.static_method_test("I do not need any object in my parameters!!"))
print(server.static_method_test("I do not need any object in my parameters!!"))
print(server) # returns __str__ method