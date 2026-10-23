while True:
    print("\n==================================")
    print("Welcome to Calculator!")
    print("Available Operations!")
    print("1. Addition : +")
    print("2. Subtraction : -")
    print("3. Multiplication : *")
    print("4. Divison : /")
    print("5. Integer Division : //")
    print("6. Remainder : %")
    print("7. Power : **")
    print("8. Exit!")
    print("\n==================================")
    userInput = int(input("Operation : "))
    print("\n==================================")
    
    if userInput == 8:
        print("\n==================================")
        print("THANK YOU FOR USING CALCULATOR")
        print("\n==================================")
        break
    
    
    a = float(input("Enter number 1 : "))
    b = float(input("Enter number 2 : "))
    
    match userInput:
        case 1:
            print(f"\nYou Chose Addition of {a} and {b} which is {a+b}")
        case 2:
            print(f"\nYou Chose Subtraction of {a} and {b} which is {a-b}")
        case 3:
            print(f"\nYou Chose Multiplication of {a} and {b} which is {a*b}")
        case 4:
            print(f"\nYou Chose Divison of {a} and {b} which is {a/b}")
        case 5:
            print(f"\nYou Chose Integer Division of {a} and {b} which is {a//b}")
        case 6:
            print(f"\nYou Chose Remainder of {a} and {b} which is {a%b}")
        case 7:
            print(f"\nYou Chose Power of {a} and {b} which is {a**b}")
        case _:
            print("\nINCORRECT OPTION PLEASE ENTER A VALID OPTION LISTED BELOW!")
        