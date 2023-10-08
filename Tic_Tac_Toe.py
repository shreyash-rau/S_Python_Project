

# to preserved the overdrive the sum, so we create sun funciton 
def sum(a, b, c ):
    return a + b + c

def BoardOfGame(xState, oState):
    zer = "X" if xState[0] else ("O" if oState[0] else 0 )
    one = "X" if xState[1] else ("O" if oState[1] else 1 )
    two = "X" if xState[2] else ("O" if oState[2] else 2 )
    three = "X" if xState[3] else ("O" if oState[3] else 3 )
    four = "X" if xState[4] else ("O" if oState[4] else 4 )
    five = "X" if xState[5] else ("O" if oState[5] else 5 )
    six = "X" if xState[6] else ("O" if oState[6] else 6 )
    seven = "X" if xState[7] else ("O" if oState[7] else 7 )
    eight = "X" if xState[8] else ("O" if oState[8] else 8 )

    print(f"_____________")
    print(f"| {zer} | {one} | {two} |")
    print(f"|---|---|---|")
    print(f"| {three} | {four} | {five} |")
    print(f"|---|---|---|")
    print(f"| {six} | {seven} | {eight} |")
    print(f"-------------")

# create function to check which player is win 
def checkWinner(xState, oState):
    # taking possible combination of winners in List wise index
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[1,4,8],[2,4,6]]
    for win in wins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("1st Player Won the Match")
            return 1
        if (sum(oState[win[0]], oState[win[1]], oState[win[2]]) == 3):
            print("2nd Player Won the Match")
            return 0
    return -1    


# when we run our program help to ensure its 
# import only function not code 
if __name__ == "__main__":

    xState = [0, 0, 0, 0, 0, 0, 0 ,0,0 ]
    oState = [0, 0, 0, 0, 0, 0, 0 ,0,0 ]
    # consider the 1 as x and o as 0 turn
    turn = 1
    print("Welcome to Tic Tak Toe")
    while(True):
        BoardOfGame(xState, oState)
        if (turn == 1):
            print("1st Player Chance ")
            value = int(input("Plse Enter the value - "))
            xState[value] = 1
        else:    
            print("2nd Player Chance ")
            value = int(input("Plse Enter the value - "))
            oState[value] = 1

# to check which player won the match 
# to not get error while running store the checkWinner in seperat variabel
        winner = checkWinner(xState, oState)
        if (winner != -1):
            print("Match Over")
            break
                    
# to take the chance of 2nd player it turn = 1 then 1 - 1 = 0 so 2nd player get chnce
        turn = 1 - turn    






