# class Person:
#     # name = ''
#     # age = ''
#     # complexion = ''
#     # height = ''
#     # gender = ''
#     def __init__(self, name, age, complexion, height, gender): 
#         self.name = name #
#         self.age = age
#         self.complexion = complexion
#         self.height = height
#         self.gender = gender
    
#     def speak(self):
#         print('Hello! How are you?')
    
# person1 = Person("favour", 25, "black", 170, "male")
# # person1.speak()
# print(person1)
# # print(type(person1))


# class Book:
#     def __init__(self, title, author, publisher, date, price):
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#         self.date = date
#         self.price = price

# book1 = Book("Python for Everyone", "Mr.John", "Techrise", 2021, "€100")
# print(book1.author)

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.__password = password
        
#     def get_password(self):
#         return self.__password
        
# user1 = User(input("Pick a username: "), input("Pick a password: "))
# # user1 = User("lenovo", "123456")
# print(user1.username)
# print(user1.get_password())

class Animal:
    def __init__(self, name, breed, colour, animal_type):
        self.name = name
        self.breed = breed
        self.colour = colour
        self. animal_type = animal_type
        
    def get_details(self):
        return f"Type: {self.animal_type} \nBreed: {self.breed} \nColour: {self.colour} \nName: {self.name}"
    
class Dog(Animal):
    def speak(self):
        return "wuff wuff"
dog1 = Dog("Raven", "Golden Retriever", "Brown", animal_type="Dog")
print(dog1.get_details())

class Cat(Animal):
    def speak(self):
        return "miaw miaw"    
cat = Cat("Garfield", "Stubby", "Orange", animal_type="Cat")

class Bird(Animal):
    def speak(self):
        return "chirp chirp"
bird = Bird("Parrot", "Blue", "Blue", animal_type="Bird")

print(dog1.speak(), cat.speak(), bird.speak())
for animal in [dog1, cat, bird]:
    print(animal.get_details())