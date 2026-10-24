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

# Task 6 – Personalized Greeting

# Create a function named greetUser(name) that accepts a name as a parameter and prints a personalized greeting.

# Example:
# greetUser("Yash")
# greetUser("Pavan")

# Expected Output:
# Hello Yash! Welcome to Python.
# Hello Pavan! Welcome to Python.


# def greetUser(name):
#     print(f"Hello {name}! Welcome to Python")

# greetUser("Yash")
# greetUser(name = "Pavan")




""" 
Task 7 – Age Eligibility Checker

Create a function named checkAge(name, age) that:
- Prints the person's name.
- If age is 18 or above, prints "You are eligible to vote."
- Otherwise, prints "You are not eligible to vote yet."
Example:
checkAge("Yash", 20)
checkAge("Rahul", 16)
"""

# def checkAge(name, age):
#     print(name)
#     if age >= 18:
#         print("You are eligible to vote.")
#     else:
#         print("You are not eligible to vote yet.")

# checkAge("Yash", 20)
# checkAge("Rahul", 16)



"""
Task 8 – Calculator

Create a function named calculator(a, b) that prints the following operations:
- Addition
- Subtraction
- Multiplication
- Division
Example:
calculator(10, 5)

Expected Output:
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0

Handle division by zero using an if statement.
"""

# def calculator(a, b):
#     print("Addition: ", a+b)
#     print("Subtraction: ", a-b)
#     print("Multiplication: ", a*b)
#     if b != 0:
#         print("Division: ", a/b)
#     else:
#         print("You cannot divide by Zero!")
#     print()

# calculator(10, 5)
# calculator(b=5, a=7)


"""
Task 9 – Multiplication Table Generator

Create a function named table(number) that prints the multiplication table of the number passed as an argument, 
from 1 to 10.

Example:
table(7)
table(12)

The same function should work for different numbers without changing its code.
"""

# def table(n):
#     print("-"*20)
#     for i in range(1, 11):
#         print(f"| {n} * {i} = {n*i}\t|")
#     print("-"*20)

# table(5)
# table(12)

"""
Task 10 – Number Analyzer

Create a function named analyzeNumber(number) that performs the following tasks:
1. Prints whether the number is positive, negative, or zero.
2. Checks whether the number is even or odd.
3. Prints the square of the number.
4. Prints the multiplication table of the number from 1 to 10.
Example:
analyzeNumber(4)

Expected Output:
Number is positive.
Number is even.
Square: 16

Multiplication Table:
4 x 1 = 4
4 x 2 = 8
...
4 x 10 = 40
"""

# def analyzeNumber(n):
#     if n > 0:
#         print(f"Number {n} is Positive")
#     elif n < 0:
#         print(f"Number {n} is Negative")
#     else:
#         print(f"Number {n} is Zero")

#     if n % 2 == 0:
#         print(f"{n} is Even!")
#     else:
#         print(f"{n} is Odd!")

#     print("Square :", n ** 2)

#     table(n)

# analyzeNumber(-52)




"""
Return Statement 

It is used to return any Data to the called function
It ends the function execution when run, it can be used to Return Nothing and Some data as well
"""

# def simpleInterest(P, R, T):
#     SI = (P*R*T)/100
#     return SI


# p = 20000
# r = 7
# t = 3
# interest = simpleInterest(p,r,t)
# print(p)
# print(interest)
# print(interest + p)



# area of Sphere 
# def areaOfSphere(r):
#     return 4 * 3.1415 * r

# print(areaOfSphere(4))
# print(areaOfSphere(6))


# def fact(number):
#     n = 1
#     for i in range(1, number+1):
#         n *= i    
#     return n



# n = int(input("Enter n value : "))
# r = int(input("Enter r value : "))
# n_minus_r = n - r

# combination = fact(n) / (fact(n_minus_r)*fact(r))
# print(combination)



""" 
Syntax

def function_name(parameters):
    # code
    # optional return statement

# Function with No Parameter and No Return Value
def greet():
    print("Hello")

# Function with Parameter and No Return Value
def greet(name):
    print(f"Hello {name}")
    
# Function without Parameter and With Return Value
def getPI():
    return 22/7

# Function With Parameter and With Return Value
def fact(number):
    n = 1
    for i in range(1, number+1):
        n *= i    
    return n
"""