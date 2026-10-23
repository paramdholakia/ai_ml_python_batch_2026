n = int(input("Enter a number : "))
counter = 0
while True:    
    print(counter, end=" ")
    if counter == n:
        break 
    counter = counter + 1

print("Loop Ended")