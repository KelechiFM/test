# def greet ():
#     print ("Hello, Faith!")
# greet ()

# def greet_user (name = "Faith", age = 23):
#     print (f" Hello {name}, you are {age} years old.")
# greet_user()

# def greet_user (name = "Sunday"):
#     print (f" Hello {name}")
    
# greet_user()
# greet_user ("Cynthia")

# numbers = [1, 2, 3, 4]
# squared_numbers = list (map (lambda x: x ** 2, numbers))
# print (squared_numbers)

# def multiply (a, b):
#     result = a * b
#     return result

# product = multiply (15, 3)
# print (product)

# def calculate_area (length = 6, width = 6):
#     area = length * width
#     return area
# area = calculate_area()
# print (area)
    
# def greet_person (name, greeting= "Hello"):
#     print (f"{greeting} {name}, you are welcome")
# greet_person("Faith")
# greet_person( "Good morning")

# Regular function
# def add(x, y):
#     return x + y

# # Lambda function
# add = lambda x, y: x + y

# print(add(5, 3))  # Output: 8

# Lambda functions are often used with functions like map(), filter(), and sorted().
# Example using map() with a lambda function:
# python
# Copy code
# numbers = [1, 2, 3, 4]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)  # Output: [1, 4, 9, 16]

# def multiply(x, y):
#     return x * y
# multiply = lambda x, y: x * y
# print (multiply(7, 8))

# def multiply (a, b):
#     return a * b

# multiply = lambda a, b: a * b
# print (multiply(10, 3))

def multiply(a, b):
    result = a * b
    return result

product = multiply(5, 3)
print(product)  # Output: 15


def get_min_max ():