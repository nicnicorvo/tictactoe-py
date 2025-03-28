# TIC-TAC-TOE GAME
# Made by Nick, for Charlotte
# 03/24/2025

# TO-DO: Game Mechanics (Winning or Losing)

grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
playerOneTurn = True
gameOver = 0

def generateGrid():
    for i in range(3):
        print(f"___________")
        for j in range(3):
           print(grid[i][j], "| ", end='')
        print('')

def checkWin():
    # TO-DO: Write Function to check if 3 in a row, column, or diagonal
    # 0 = No Winner, 1 = X Won, 2 = O Won, 3 = Tie

    # Check rows for a winner:
    for row in range(3):
        if (grid[row][0] == grid[row][1] == grid[row][2] != ' '):
            return 1 if grid[row][0] == 'X' else 2
    
    #Check columns for a winner:
    for col in range(3):
        if (grid[0][col] == grid[1][col] == grid[2][col] != ' '):
            return 1 if grid[0][col] == 'X' else 2
    
    # Check diagonals for a winner:
    if (grid[0][0] == grid[1][1] == grid[2][2] != ' '):
        return 1 if grid[0][0] == 'X' else 2
    if (grid[0][2] == grid[1][1] == grid[2][0] != ' '):
        return 1 if grid[0][2] == 'X' else 2
    
    # Check for a tie (full board, no winner):
    is_tie = True
    for row in range(3):
        for col in range(3):
            if (grid[row][col] == ' '):
                is_tie = False
                break
        if not is_tie:
            break
    
    if (is_tie):
        return 3
    
    # Return 0 if no winner yet:
    return 0

def placeExOrOh(gridPosition):
    correctNumber = True
    if ((gridPosition >= 0) and (gridPosition <= 2)):
        if (grid[0][gridPosition] == ' '):
            if (playerOneTurn):
                grid[0][gridPosition] = 'X'
                return correctNumber
            else:
                grid[0][gridPosition] = 'O'
                return correctNumber
        else:
            print(f"ERROR: Slot Already Filled")
            correctNumber = False
            return correctNumber
    elif ((gridPosition >= 3) and (gridPosition <= 5)):
        if (grid[1][gridPosition - 3] == ' '):
            if (playerOneTurn):
                grid[1][gridPosition - 3] = 'X'
                return correctNumber
            else:
                grid[1][gridPosition - 3] = 'O'
                return correctNumber
        else:
            print(f"ERROR: Slot Already Filled")
            correctNumber = False
            return correctNumber
    elif ((gridPosition >= 6) and (gridPosition <= 8)):
        if (grid[2][gridPosition - 6] == ' '):
            if (playerOneTurn):
                grid[2][gridPosition - 6] = 'X'
                return correctNumber
            else:
                grid[2][gridPosition - 6] = 'O'
                return correctNumber
        else:
            print(f"ERROR: Slot Already Filled")
            correctNumber = False
            return correctNumber
    else:
        print(f"ERROR: Number must be 0 to 8 (0 being top left corner, 8 being bottom right corner)")
        correctNumber = False
        return correctNumber

generateGrid()
# Main Loop of Program:
while (gameOver == 0):
    
    # TO-DO: Finish Logic For Winning/Losing Game
    print(f"GRID POSITIONS: 0, 1, 2 = Top Row. 3, 4, 5 = Middle Row. 6, 7, 8 = Bottom Row.")

    if (playerOneTurn):
        print(f"Current Turn: X")
    else:
        print(f"Current Turn: O")

    # Error handling for catching non-integers:
    try:
        choice = int(input("Enter which position: "))
    except ValueError:
        print("ERROR: Input must be a valid integer (whole number).")
        continue
    
    # Error handling to make sure incorrect number doesn't cause change of turns:
    correctlyPlaced = placeExOrOh(int(choice))
    if (correctlyPlaced):
        playerOneTurn = not playerOneTurn

    generateGrid()

    gameOver = checkWin()
    if ((gameOver == 1) or (gameOver == 2)):
        print(f"GAME OVER! The Winner is: ", end='')
        if (gameOver == 1):
            print("X! Thanks for playing!")
            input("Press any key to continue...")
        elif (gameOver == 2):
            print("O! Thanks for playing!")
            input("Press any key to continue...")
    elif (gameOver == 3):
        print(f"GAME OVER! It's a tie, nobody won! Thanks for playing!")
        input("Press any key to continue...")