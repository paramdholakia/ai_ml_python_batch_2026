# Escape Sequences in Python

# Strings have special characters called escape sequences that are used to represent certain characters that are difficult or impossible to type directly into a string. 
# Escape sequences are represented by a backslash (\) followed by a character.

# Note: The backslash (\) is used as an escape character in Python strings. It allows you to include special characters in a string that would otherwise be difficult to represent.


# \n	New Line	
#  \n is used to create a new line in a string. When the string is printed, the text after \n will appear on a new line.
# str = "Hello\nWorld"
# print(str)  # Output: Hello World

# \t	Tab	
# \t is used to create a horizontal tab in a string. When the string is printed, the text after \t will be indented by a tab space.
# print("Hello\tWor\tld") 


# \b	Backspace	
# print("Hello\bWorld")


# \'	Single Quote	
# "" ''

# str = 'it\'s a brand new day'
# print(str)  # Output: it's a brand new day
# str = "This is a quote : \"Hello World\""
# print(str)  # Output: This is a quote : "Hello World"


# \\	Backslash	
# print("This is a backslash: \\ ")  # Output: This is a backslash: \


# \r	Carriage Return	
# \r is used to move the cursor to the beginning of the current line. When the string is printed, the text after \r will overwrite the text before it.
# print("Hello\rWorld\r")
# World




# \f	Form Feed	
# \f is used to create a form feed in a string. When the string is printed, the text after \f will appear on a new page or form feed.
# Hello world
# print("Hello\fWorld")  # Output: Hello World

# \ooo	Octal value	(Base-8)
# print("\110\105\114\114\117")

# \xhh	Hex value	(Base-16)
# print('\x48\x45\x4C\x4C\x4F')