"""
3 Statements that control the flow of the loop
break
continue 
pass 
"""


# break is a statement which is used to terminate a loop immediately

# n = int(input("Enter a number : "))
# counter = 0
# while True:
#     print(counter, end=" ")
#     if counter == n:
#         break
#     counter = counter + 1

# print("Loop Ended")


# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)


# continue statement : if you ever want to skip an iteration of a loop then we will use continue statement

# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)

# 1 -> 10 : 5 Skip

# i = 1
# while i <= 10:
#     if i == 5:
#         # i += 1
#         continue
#     print(i)
#     i += 1


# pass statement
# it is used to do nothing

# n = 7
# if n % 7 == 0:
#     print("This number is divisible by 7")
#     pass
# print("Task Finished")

# print("Hello World")

# for i in range(1, 6):
#     if i % 2 == 0:
#         # print("Even Number")
#         pass
#     else:
#         print(i)


# ----------------------------------------------------------------------------

""" 
Print numbers from 1 to 50:
Skip even numbers using continue
Stop when the number reaches 35.
"""
# for i in range(1, 51):
#     if i % 2 == 0:
#         continue

#     if i == 35:
#         break

#     print(i)

# i = 0
# while i <= 50:
#     if i % 2 == 0:
#         continue

#     if i == 35:
#         break

#     print(i)


# Ask the user to enter 10 numbers:
# Skip negative numbers using continue
# Stop completely if the user enters 0.

# list1 = []

# while True:
#     inp = float(input("Enter a number : "))
#     if inp == 0:
#         break
#     elif inp < 0:
#         continue
#     else:
#         list1.append(inp)

# print(list1)


# Print numbers from 1 to 100:
# Skip numbers divisible by 3
# Stop when the number reaches 80.
# for i in range(1, 101):
#     if i == 80:
#         break
#     if i % 3 == 0:
#         continue
    
#     print(i)



# Ask the user to enter numbers repeatedly:
# Skip negative numbers
# Stop when the user enters 100
# Calculate the sum of all other positive numbers.

# sum = 0 

# while True:
#     userInput = int(input("Enter a number : "))
    
#     if userInput < 0:
#         continue
#     if userInput == 100:
#         break
#     sum += userInput

# print(sum)



# Search for 50 in a list:
# Skip negative numbers
# Stop when 50 is found
# Print "50 found".

# ls = [2,123,12,445,-1,346,234,-125,63,-45,234,6,-34,50,-2134,6,-34,2,-13,4,6786,75,43,344,89564,3]
# index = 0
# while index < len(ls):
#     if ls[index] == 50:
#         print("50 IS FOUND")
#         break
#     if ls[index] < 0:
#         index += 1
#         continue
#     index += 1

# for i in ls:
#     if i < 0: 
#         continue
#     if i == 50:
#         print("50 IS FOUND!")
#         break