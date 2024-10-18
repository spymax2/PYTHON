# object-oriented programming
# class should start with a capital letter
# class Person:
#     def __init__(self):
#         self.name = "Neema"
#         self.age = 40
#         self.email = "nicole36@gmail.com"
#         self.phone ="0798765432"
# person = Person()
#
# person.name = "Stew"
#
# print(person.name)
# print(person.age)
# print(person.email)
# print(person.phone)

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person1 = People("Ashley",12)

person2 = People("Ruth",30)

print(f" my name is {person2.name} ,my age is {person2.age}")







