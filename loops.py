""" 
Loops are used to execute a block of code repeatedly until a certain condition is met. 
In Python, there are two main types of loops: for loops and while loops.

For loops and While loops are both Entry Controolled Loops. 
In Entry Controlled Loops, the condition is checked before executing the loop body.
"""

""" 

range(start, stop, step=1)

range(0,10) => 0,1,2,3,4,5,6,7,8,9


For Loop:

Syntax : 

for iterable in sequence:
    # block of code to be executed

range() function is used to generate a sequence of numbers.

range(1,11) => 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
                                           ^
                                           |
                                           i
"""

# for i in range(1, 11):
#     print(i)

# for i in range(1, 11):
#     print(i, "Hello World!")

# Print 1 to 100

# for number in range(1, 101):
#     print(number, end=" ")


# Take two input from user and print all the numbers between those two numbers
# using for loop

# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))

# for i in range(start, end + 1):
#     print(i, end=" ")


# for i in range(5, 0, -1):
#     print(i)

# Take two input from user and print all the numbers between those two numbers
# if it is even print "Even Number N" and if it is odd print "Odd Number N"

# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))

# for i in range(start, end + 1):
#     if i % 2 == 0:
#         print("Even Number", i)
#     else:
#         print("Odd Number", i)


# 1. Print all numbers between 50 and 100 that are divisible by 4.
# for i in range(50, 101):
#     if i % 4 == 0:
#         print(i, end=" ")

# 2. Find the sum of all numbers between 1 and 100 that are divisible by 7.

# sum = 0
# for i in range(1, 101):
#     if i % 7 == 0:
#         print(i, sum, sum + i, sep=" | ")
#         sum += i

# print(sum)

# 3. Find the product of all numbers from 1 to 10.
# temp = 1
# for i in range(1, 11):
#     temp = temp * i
# print(temp)

""" 
temp = 1
i : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    temp    i   temp = temp * i
    1       1   1
    1       2   2  
    2       3   6   
    6       4   24
    24      5   120   
    120     6   720   
    720     7   5040   
    5040    8   40320  
    40320   9   362880   
    362880  10  3628800  
"""


# 4. Print the square of every number from 1 to 15.
# for i in range(1, 16):
#     print(i ** 2, end=" ")

# 5. Print the cube of every number from 1 to 10.
# for i in range(1, 11):
#     print(i ** 3, end=" ")


# 6. Take a number from the user and print all its factors.
# n = int(input("Enter a value : "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=" ")

# 7. Take a number from the user and count how many factors it has.
# n = int(input("Enter a value : "))
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1 # count = count + 1

# print(count)

# 8. Take a number from the user and calculate the sum of all its factors.
# n = int(input("Enter a value : "))
# sum = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         sum += i
# print(sum)


# 9. Take a number from the user and check whether it is a perfect number.
# 6 : 1 2 3
# 1 + 2 +3 = 6

# 28 : 1 2 4 7 14
#  1 + 2 + 4 + 7 + 14 = 28

# n = int(input("Enter a value : "))
# sum = 0

# for i in range(1, n):
#     if n % i == 0:
#         sum += i

# if sum == n:
#     print("A perfect number!")
# else:
#     print("NOT A perfect number!")


# 10. Take a number from the user and check whether it is a prime number.
# 7 -> 2, 3, 4, 5, 6
# 6 -> 2, 3, 4, 5
n = int(input("Enter a anumber : "))
flag = True

for i in range(2, n):
    if n % i == 0:
        flag = False

if flag == True:
    print("NUMBER IS PRIME")
else:
    print("NUMBER IS NOT PRIME")
