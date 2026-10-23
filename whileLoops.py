""" 
Loops : We use loop to repeat a certain code N number of times that we specify in it.

While loop : its a type of loop which always runs on a condition

Syntax : 
while conditon: 
    # Piece of code to be excecuted while the condition remains true
    
    # statement to ensure termination after a point
"""

# number = int(input("Enter a number : "))

# while number >= 0:
#     print(number)
#     number -= 1    # number = number - 1

""" 
numebr = 3

is number >= 0? 3 >= 0 : Yes
Print 3 
number = 3-1 = 2

is number >= 0? 2 >= 0 : Yes
Print 2 
number = 2-1 = 1

is number >= 0? 1 >= 0 : Yes
Print 1 
number = 1-1 = 0

is number >= 0? 0 >= 0 : Yes
Print 0 
number = 0-1 = -1

is number >= 0? -1 >= 0 : NO
"""


# 1. Print numbers from 1 to 10 using a while loop.
# number = 1
# while number < 11:
#     print(number, end=" ")
#     number += 1

# 2. Print numbers from 10 to 1 using a while loop.
# number = 10
# while number > 0:
#     print(number)
#     number -= 1

# 3. Print all even numbers from 1 to 20.
# n = 1
# while n <= 20:
#     if n % 2 == 0:
#         print(n, end=" ")
#     n += 1

# 4. Print all odd numbers from 1 to 20.
# n = 1
# while n <= 20:
#     if n % 2 != 0:
#         print(n, end=" ")
#     n += 1

# 5. Print the multiplication table of a number entered by the user.
# n = int(input("Enter a number : "))
# multiplier = 1

#  n X multiplier = n*multipler
# while multiplier < 11:
#     print(f"{n} X {multiplier} = {n * multiplier}")
#     multiplier += 1


# 6. Print numbers from 1 to N, where N is entered by the user.
# n = int(input("Enter a number : "))
# counter = 1
# while counter <= n:
#     print(counter)
#     counter += 1


# 7. Find the sum of numbers from 1 to N.
# n = int(input("Enter a number : "))
# counter = 1
# sum = 0
# while counter <= n:
#     sum += counter
#     print(counter, sum)
#     counter += 1

# 8. Find the sum of all even numbers from 1 to N.

# n = int(input("Enter a number : "))
# counter = 1
# sum = 0

# while counter <= n:
#     if counter % 2 == 0:
#         print(counter, end="+")
#         sum += counter
#     counter += 1

# print(f"\n{sum}")


# 9. Find the sum of all odd numbers from 1 to N.
# n = int(input("Enter a number : "))
# counter = 1
# sum = 0

# while counter <= n:
#     if counter % 2 != 0:
#         print(counter, end="+")
#         sum += counter
#     counter += 1

# print(f"\n{sum}")

# 10. Print the squares of numbers from 1 to 10.
# i = 1
# while i <= 10:
#     print(i ** 2)
#     i += 1

# 11. Print the cubes of numbers from 1 to N.

# 12. Count how many numbers are divisible by 3 between 1 and N.

# 13. Count how many even numbers are present between two numbers entered by the user.

# 14. Find the factorial of a number using a while loop.

# 15. Take a number from the user and print its digits one by one.
#     Example: 5832 → 2, 3, 8, 5

# number = 123
# for i in str(number) :
#     print(i, end=", ")

# /, %
# / : it returns the result after division
# % : it returns the result after divison and that result is our First remainder

# number = int(input("Input a number : "))
# last_digit = None
# digits = []
# while number >= 1:
#     last_digit = number % 10
#     digits.insert(0, last_digit)
#     number = number // 10
# print(digits)


# 16. Count the number of digits in a number.
#     Example: 5832 → 4 digits
# number = int(input("Input a number : "))
# count = 0
# while number >= 1:
#     number = number // 10
#     count += 1
# print(count)


# 17. Find the sum of the digits of a number.
#     Example: 5832 → 18
# number = int(input("Input a number : "))
# last_digit = None
# sum = 0
# while number >= 1:
#     last_digit = number % 10
#     print(last_digit, end="+")
#     sum += last_digit
#     number //= 10  # number = number // 10

# print("=", sum)

# 18. Reverse a number using a while loop.
#     Example: 5832 → 2385
# number = int(input("Enter a number : "))
# reverse = 0
# while number >= 1:
#     reverse = (reverse*10) + (number % 10)
#     number //= 10
# print(number, reverse)


""" 
number = 123
rev = 321
temp = 0

    number % 10     number//=10     temp = (temp * 10) + (number % 10)
    3               12              (0 * 10) + 3 = 3 
    2               1               (3 * 10) + 2 = 32
    1               0               (32 * 10) + 1 = 321


number = 5792
rev = 2975
temp = 0
    number % 10     number//=10     temp = (temp * 10) + (number % 10)
    2               579             (0 * 10) + 2   = 2
    9               57              (2 * 10) + 9   = 29
    7               5               (29* 10) + 7   = 297
    5               0               (297*10) + 5   = 2975
"""


# 19. Keep asking the user to enter a password until they enter "python123".

# password_input = input("Please enter your password : ")

# while password_input != "python123":
#     password_input = input("Please enter your password : ")

# print("Login")

# 20. Keep asking the user to enter numbers until they enter 0.
#     Then print the sum of all the numbers entered.
# number = int(input("Enter a number : "))
# sum = 0
# while number != 0:
#     sum += number
#     number = int(input("Enter a number : "))
    
# print(sum)