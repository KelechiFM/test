# class Animal:
#     # type = ""
#     # name = ""
#     # feed = ""
#     def __init__(self, type, name, feed):
#         self.type = type
#         self.name = name
#         self.feed = feed
    #for method
    # def describeobj (self):
        # return f"The animal object is {self.name} and its of the family {self.type} and it eats {self.feed}"
        


# animal1 = Animal('mammals', 'Goat', 'Weeds')
# # animal1.type = "mammals"
# # animal1.name = "Goat"
# # animal1.feed = "Weeds"

# animal2 = Animal("Aves", "Chicken", "Chicken Feeds")
# # animal2.type = "Aves"
# # animal2.name = "Chicken"
# # animal2.feed = "Chicken Feed"

# print(f"The first animal object is {animal1.name} and its of the family {animal1.type} and it eats {animal1.feed}")
# # print(f"The second animal object is {animal2.name} and its of the family {animal2.type} and it eats {animal2.feed}")


# excersise
# create an electronic class
# objects: phone, television, laptop, microwave, blender
# attributes: make, model, year, type
# method: description: describing the make, model

# print(animal1.describeobject())

class Electronic:
    def __init__(self, make, model, year, type):
        self.make = make
        self.model = model
        self.year = year
        self.type = type
        
        
#     def describeobject (self):
#         return f"This is a smart {self.make} and {self.model}, and {self.year}, {self.type}"

# phone = Electronic ("iphone", "iphone 16 pro max", "2024", "iphone")
# print (phone.describeobject ())

# television = Electronic ("samsung", "52 inches", "2023", "smart tv" )
# print (television.describeobject())

# laptop = Electronic ("alienware", "gaming laptop", "2023", "light weight")
# print (laptop.describeobject())

# microwave = Electronic ("hisense", "32 inches", "2022", "inverter microwave")
# print (microwave.describeobject())

# blender = Electronic ("decker", "home appliance", "2023", "hand blender")
# print (blender.describeobject())


# class Animal:
#     def __init__(self, type):
#         self.type = type
        
#     def describe(self):
#         # Method
#         return f"This animal belongs to the {self.type} family"
    
# class Dog (Animal):
#     """ Child Class
#     """
#     def __init__(self, type, name, feed):
#         super().__init__(type)
#         self.name = name
#         self.feed = feed
        
#     def bark (self):
#         # Method
#         return f"The {self.name} is barking woof woof woof"
    
# dog1 = Dog ("mammal", "ruddy", "Dog feed")

# print(dog1.describe())
# print(dog1.bark())

