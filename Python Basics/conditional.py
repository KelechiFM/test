# age = 18
# if age >= 18:
#     print ("you are eligible to vote.")
    
# age = 20
# has_voter_id = True

# if age >= 18 and has_voter_id:
#     print ("You are eligible to vote.")
    
# else:
#     print ("You are not eligible to vote.")

# temperature = 20

# if temperature > 25:
#     print ("its's a hot day!")
# else:
#     print ("it's not too hot")

# score = 99

# if score >= 90:
#     print ("Grade: A")
# elif score >= 80:
#     print ("Grade: B")
# elif score >= 70:
#     print ("Grade: C")
# elif score >= 50:
#     print ("Grade: D")
# elif score >= 45:
#     print ("Grade: E")
# else:
#     print ("Grade: F")

# age = 10
# is_registered = True

# if age >= 18:
#     if is_registered:
#         print("You are eligible to vote.")
#     else:
#         print ("you need to register to vote.")
# else:
#     print ("you are not old enough to vote.")

# age = 15

# if age < 18:
#     print ("you are a minor.")

# age = int (input ("Enter your age: "))

# if age >= 18:
#     print ("you are legally allowed to drive.")
    
# password = str (input ("Enter your password: "))

# if password == "secret":
#     print("Acess Granted.")
# else:
#     print ("Fuck off")

# hour = int (input ("Enter your current time: "))

# if hour <= 12:
#     print ("Good morning")
# elif hour <= 17:
#         print ("Good afternoon!")
# elif hour >= 17:
#     print ("Good evening")

# number = float (input("Enter a number"))

# if number > 0:
#     print ("This is a positive number")
# elif number < 0:
#     print ("This is a negative number")
# else:
#     print ("You've entered zero")

num1 = float (input("Enter the first number: "))
num2 = float (input ("Enter the second number: "))
num3 = float (input ("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print (f"The largest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print (f"The largest number is {num2}")
else:
    print(f"The Largest number is: {num3}")

    

