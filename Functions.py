""" 
Functions in Python 

A function in Python is a reusable block of organized, indented code used to perform a single, focused action. 
Instead of writing the same code repeatedly, you pack the logic into a function and "call" it whenever needed, 
which makes your programs more modular, readable, and easier to maintain.

Syntax : 

def function_name(parameters):
    # function_body
    # optional return statement

---------------------------
Function with No Parameter and No Return Statement

def helloWorld():
    print("Hello World")

helloWorld() # Calling a function
    

---------------------------
Function with Parameters

def licenseChecker(name, age): # Variables in Functions are called Parameters
    print(f"Hello {name}!")
    if age > 18 : 
        print("You are eligible for 4 Wheeler License")
    elif age > 16 :
        print("You are eligible for 2 Wheeler Non Geared License")
    else:
        print("You are not eligible for License")


licenseChecker("Yash", 20) # Whenever you call a function, with Data in Parantheses they are called Arguements

---------------------------



"""

def licenseChecker(name, age):
    print(f"Hello {name}!")
    if age > 18 : 
        print("You are eligible for 4 Wheeler License")
    elif age > 16 :
        print("You are eligible for 2 Wheeler Non Geared License")
    else:
        print("You are not eligible for License")


licenseChecker("Yash", 20)
licenseChecker("Anandi", 18)
licenseChecker("Tirth", 15)






# n = int(input("Enter n value : "))
# r = int(input("Enter r value : "))
# n_minus_r = n - r


