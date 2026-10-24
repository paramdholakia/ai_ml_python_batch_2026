""" 
Nested Loops are the type of loops, when we place a loop insde another loop
whenever we write nested loops, it runs in NxM times
"""

# print N*M Stars : N stars (Rows) in M Columns

# n = int(input("Enter number of Rows : "))
# m = int(input("Enter number of Columns : "))

# for i in range(n):
#     for j in range(m):
#         print("*",end="")
#     print("")
    
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)
        
# for i in range(0, 5):
#     for j in range(0, i+1):
#         print("*", end="")
#     print()
"""
*****
****
***
**
*
"""
# n = int(input("Enter number of Rows : "))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


""" 
*
**
***
****
*****
****
**
*
"""
# n = int(input("Enter number of Rows : "))

# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(n-1, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()
    
"""
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
"""
# n = int(input("Enter a number : "))
# for i in range(1, n+1):
#     for j in range(n-i):
#         print(' ', end="")
        
#     for j in range(i):
#         print("*", end=" ")
#     print()

""" 
* * * * *
 * * * *
  * * *
   * *
    *
"""

# for i in range(5, 0, -1):
#     for j in range(5 - i):
#         print(" ", end="")
        
#     for j in range(i):
#         print("*", end=" ")
        
#     print() 
    
""" 
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





# ---------------------------------------------------------------

# list1 = [1,2,3,4,5,6,7,8,9]

# for i in range(9):
#     print(list1[i])

# for i in list1:
#     print(i)

list1 = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
]

# for i in range(3):
#     for j in range(3):
#         print(list1[i][j], end=" ")
#     print()

# for i in list1:
#     for j in i:
#         print(j, end=" ")
#     print()


""" 
i j
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
"""
# Access a specific column
# list1 = [
#     [1,2,3], 
#     [4,5,6], 
#     [7,8,9]
# ]

# list1[rowNumber][colNumber]
# column = int(input("Enter a column 0-2"))

# for i in range(3):
#     print(list1[i][column], end=" ")

list1 = [
  #  0,1,2 
    [1,2,3], # 0 
    [4,5,6], # 1
    [7,8,9]  # 2
]

# for i in range(2, -1, -1):
#     for j in range(2, -1, -1):
#         print(list1[i][j], end=" ")
#     print()

# --------------
# i = len(list1) - 1
# j = len(list1[0]) - 1

# while i >= 0:
#     print(list1[i][j])

#     j -= 1
#     if j < 0:
#         i -=1
#         if i >= 0:
#             j = len(list1[i]) - 1
# --------------------



# list1 = [
#   #  0,1,2,3,4 
#     [1,2,3,4,5], # 0 
#     [6,7,8,9,10], # 1
#     [11,12,13,14,15]  # 2
# ]
# if element is even, find it's square
# if element is odd, find it's division by 5

# for i in list1:
#     for j in i:
#         if j % 2 == 0:
#             print(j**2, end=" ")
#         else:
#             print(j/5, end=" ")
#     print()


# Get me the Row sum of List1
# list1 = [
#   #  0,1,2,3,4 
#     [1,2,3,4,5], # 0 
#     [6,7,8,9,10], # 1
#     [11,12,13,14,15]  # 2
# ]

# for i in range(3):
#     sum = 0
#     for j in range(5):
#         sum += list1[i][j]
    
#     for j in range(5):
#         print(list1[i][j], end="\t")
    
#     print("\t=",sum)

# for i in list1:
#     sum = 0
#     for j in i:
#         sum += j        
#     for j in i:
#         print(j, end=" ") 
#     print(" =", sum)



# Get me the Column sum of List1
"""
1   2   3   4   5
6   7   8   9   10
11  12  13  14  15
_______________________________
18  21  24  27  25 = Column Sum
"""
list1 = [
  #j 0,1,2,3,4            i
    [1,2,3,4,5],        # 0 
    [6,7,8,9,10],       # 1
    [11,12,13,14,15]    # 2
]
# 1 6 9  : 0,0 1,0 2,0
# 2,7,12 : 0,1 1,1 2,1
# 3,8,13 : 0,2 1,2 2,2
# 4,9,14 : 0,3 1,3 2,3
# 5,10,15: 0,4 1,4 2,4




# colSum = []
# for i in range(5):
#     sum = 0
#     for j in range(3):
#         sum += list1[j][i]
#     colSum.append(sum)

# for i in list1:
#     for j in i:
#         print(j, end="\t")
#     print()
# print("-----------------------------")
# for i in colSum:
#     print(i, end="\t")



list1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# Diagonal Sum : 1 + 5 + 9 = 15



# ------------------------------------------

list1 = [1,2,3,4,5,6,7,8,9,10]

target = int(input("Enter a number : "))
flag = False

for i in range(0, 10):
    for j in range(i+1, 10):
        if list1[i] + list1[j] == target:
            print("Indices found : ",i, j)
            print("Values :", list1[i], list1[j])
            flag = True

    if flag:
        break

""" 
target = 12

Index   0   1   2   3   4   5   6   7   8   9
        1   2   3   4   5   6   7   8   9   10
        i
            j
"""


