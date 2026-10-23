""" 
Keep on Playing, until One player earns 5 Points

take 2 inputs of 2 users
compare 2 input
p1 == rock
p2 == scissors (p1), 
    (p2 == rock, tie )
    (p2 == paper, p2)
"""
p1Score = 0
p2Score = 0
    
while True:
    if p1Score == 5 or p2Score == 5:
        break
    
    print("\nWelcome to Rock Paper Scissors!")
    print("Rock : 0")
    print("Paper : 1")
    print("Scissor : 2")
    
    p1Input = int(input("P1 : Enter your Move : "))
    p2Input = int(input("P2 : Enter your Move : "))

    result = (p1Input - p2Input + 3) % 3
    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("Player 1 wins!")
        p1Score += 1
    else:
        print("Player 2 wins!")
        p2Score += 1

    print("\n=============================")
    print("==========SCOREBOARD=========")
    print("Player 1 Score : ", p1Score)
    print("Player 2 Score : ", p2Score)
    print("=============================\n")



"""
    if p1Input == 0:
        if p2Input == 1:
            p2Score += 1
            print("Player 2 Wins")
        elif p2Input == 2:
            p1Score += 1
            print("Player 1 Wins")
        else:
            print("ITS A TIE")
    elif p1Input == 1:
        if p2Input == 2:
            p2Score += 1
            print("Player 2 Wins")
        elif p2Input == 0:
            p1Score += 1
            print("Player 1 Wins")
        else:
            print("ITS A TIE")
    else:
        if p2Input == 1:
            p2Score += 1
            print("Player 2 Wins")
        elif p2Input == 2:
            p1Score += 1
            print("Player 1 Wins")
        else:
            print("ITS A TIE")
"""