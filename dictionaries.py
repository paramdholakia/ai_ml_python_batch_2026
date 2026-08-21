"""

1 : Rahul Sharma
2 : Jaydeep Verma
3 : Harsh Shah
4 : Tirth Solanki
5 : Rudra Soni
6 : Harsha Thakkar
7 : Priya gohil

# Dictionaries are type of Data which is used to store data in key value pairformat.
# It is mutable and ordered collection of data. 
# It is defined by using curly braces {}.

# IN PYTHON VERSION 3.6 AND BEFORE THE DICTIONARIES WERE UNORDERED COLLECTION OF DATA 
# BUT IN PYTHON VERSION 3.7 AND AFTER THE DICTIONARIES ARE ORDERED COLLECTION OF DATA.
 
{
    key : value,
    key : value,
    key : value,
    key : value
}

{1,2,3} # SET 
"""

studentData = {
# keyValues : DataValues
        1 : "Rahul Sharma",
        2 : "Jaydeep Verma",
        3 : "Harsh Shah",
        4 : "Tirth Solanki",
        5 : "Rudra Soni",
        6 : "Harsha Thakkar",
        7 : "Priya gohil"
}
# print(studentData)
# print(type(studentData))

# ------------------------------------------------------------------
# How to retrieve data from dictionary using key values.
# print(studentData[5])
# print(studentData[12554])

# get() method is used to retrieve data from dictionary using key values.
print(studentData.get(2))
print(studentData.get(24))

print(studentData.get(24, "STUDENT DATA DOESN'T EXIST"))

# ------------------------------------------------------------------
