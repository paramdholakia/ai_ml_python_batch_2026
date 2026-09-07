l1 = [1,2,3,4,5]
l2 = l1
l3 = [1,2,3,4,5]


# is : It checks whether two variables point to the same object in memory or not. 
# It returns True if both variables point to the same object, 
# otherwise it returns False. 


# is not : It checks whether two variables point to different objects in memory or not. 
# It returns True if the variables point to different objects, otherwise it returns False.


# print(l1 == l2)
# print(l1 == l3)
# print(l2 == l3)

# print(l1 is l2)
# print(l1 is l3)


print(l1 is not l2)
print(l2 is not l3)