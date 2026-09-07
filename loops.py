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



# Exercise 1. Print first 10 natural numbers using FOR loop
# for i in range(1, 11):
#     print(i)

# Exercise 2. Display numbers from -10 to -1 using for loop
# for i in range(-10, 0, 1):
#     print(i, end=" ")

# Exercise 3. Display a message “Done” after successful execution of for loop

# for i in range(1, 6):
#     print(i, end=" ")
# print("Done")

# Exercise 4. Calculate the sum of all numbers from 1 to N
# N = int(input("Enter a number: "))
# sum = 0

# for i in range(1, N + 1):
#     sum += i # sum = sum + i

# print(sum)

# Exercise 5. Print multiplication table of a given number
# N = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{N} X {i} = {N * i}")

# Exercise 6. Calculate the cube of all numbers from 1 to a given number
# N = int(input("Enter a number: "))
# for i in range(1 , N + 1):
#     print(i, i ** 3)


# Exercise 7. Display numbers from a list using a loop
# list1 = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grapes"]
#                                                                         ^
#                                                                         |
#                                                                         i
# for i in range(0, len(list1)):
#     print(list1[i] ,end=" ")

# print()
# for i in list1:
#     print(i, end=" ")


# Exercise 8. Count occurrences of a specific element in a list
# list1 = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grapes",
#          "Apple" , "Cherry", "Date", "Apple"]

# count = 0
# for i in list1:
#     if i == "Apple":
#         count += 1
# print(count)

# print(list1.count("Apple"))  # Using built-in count() method


# Exercise 9. Print elements from a list present at odd index positions
# list1 = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grapes"]
# for i in range(1, len(list1), 2):
#     print(list1[i], end=" ")

# for i in range(1, len(list1)):
#     if i % 2 != 0:
#         print(list1[i], end=" ")

# Exercise 10. Print list in reverse order using a loop
list1 = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grapes"]
#         0            1       2          3      4           5         6
#         -7           -6     -5         -4      -3          -2        -1

for i in range(len(list1)-1, -1, -1):
    print(list1[i], end = ",")
print()

for i in range(-1, -len(list1) - 1, -1):
    print(list1[i], end = ",")
print()

for i in list1[::-1]:
    print(i, end=",")