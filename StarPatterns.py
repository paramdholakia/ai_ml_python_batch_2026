""" 
*****
*****
*****
*****
*****

*
**
***
****
*****

*****
****
***
**
*


    *
   * *
  * * *
 * * * *
* * * * * 

* * * * * 
 * * * * 
  * * * 
   * *
    *

    

    *
   * *
  * * *
 * * * *
* * * * * 
* * * * * 
 * * * * 
  * * * 
   * *
    *
"""


""" 
   *
  * *
 *   *
*     *
 *   *
  * *
   *
"""

# for i in range(1, 5):
#     print(" " * (4-i), end="")

#     for j in range(1, 2 * i):  
#         if j == 1 or j == 2 * i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(3, 0, -1):
#     print(" " * (4 - i), end="")

#     for j in range(1, 2*i):
#         if j == 1 or j == 2 * i - 1:
#             print("*" ,end="")
#         else:
#             print(" ", end="")
#     print()
""" 
i -> range(1,2,3,4)

i   j           
1   range(1,2)  1 -> 1
2   range(1,4)  3 -> 1,2,3
3   range(1,6)  5 -> 1,2,3,4,5
4   range(1,8)  7 -> 1,2,3,4,5,6,7
"""


""" 
*      *
**    **
***  ***
********
***  ***
**    **
*      *
"""

# for i in range(1, 5):
#     print("*"*i + " " * (2 * (4 - i)) + "*"*i)
# for i in range(3, 0, -1):
#     print("*"*i + " " * (2 * (4 - i)) + "*"*i)



# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

"""
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
5 5 5 5
"""

# for i in range(1, 6):
#     for j in range(4):
#         print(i, end=" ")
#     print()


"""
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
"""
# for i in range(4):
#     for j in range(1, 5):
#         print(j, end=" ")
#     print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

# for i in range(1,6):
#     for j in range(i):
#         print(i, end=' ')
#     print()


""" 
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
# for i in range(6,1, -1):
#     for j in range(1, i):
#         print(j, end=" ")
#     print()

"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
# for i in range(5,0,-1):
#     for j in range(i):
#         print(i, end=" ")
#     print()

""" 
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

# number = 1
# for i in range(5):
#     for j in range(i+1):
#         print(number, end=" ")
#         number += 1
#     print()

""" 
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""

# for i in range(1, 6):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

""" 
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if (i+j)%2 == 0:
#             print(1, end=" ")
#         else:
#             print(0, end=" ")
#     print()


""" 
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
"""
# for i in range(1,6):

#     for j in range(0, 5-i):
#         print("", end=" ")

#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

""" 
    1
   121
  12321
 1234321
123454321
"""
# for i in range(1,6):
#     for spaces in range(0, 5-i):
#         print("", end=" ")
#     for j in range(1, i+1):
#         print(j, end="")
#     for j in range(i-1, 0, -1):
#         print(j, end="")
#     print()

""" 
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
"""
# for i in range(1,6):
#     for spaces in range(0, 5-i):
#         print("", end=" ")
    
#     for j in range(1, i + 1):
#         print(i, end=" ")
#     print()


""" 
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
"""
n = int(input("Enter number : "))
for i in range(1, n):

    for space in range((n-1)-i):
        print("", end=" ")

    for j in range(1, i+1):
        print(j, end=" ")
    print()

for i in range(n-2, 0, -1):

    print(" " * (n-1 - i), end="")

    for j in range(1, i+1):
        print(j, end=" ")
    print()

