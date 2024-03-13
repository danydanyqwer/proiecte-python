def initialPlayerChoose():
    playerSign[1] = input('Player 1, choose if you want to be X or O: ')

    while playerSign[1] not in ['X', 'O', 'x', 'o']:
        playerSign[1] = input('Invalid input! Choose if you want to be X or O: ')

    if playerSign[1] in ['X', 'x']:
        playerSign[1] = playerSign[1].upper()
        playerSign[2] = 'O'
    elif playerSign[1] in ['O', 'o']:
        playerSign[1] = playerSign[1].upper()
        playerSign[2] = 'X'

    print(f'Player 1 goes first as {playerSign[1]}.')
def printBoard():
    print(' '+indexList[1]+' '+'|'+' '+indexList[2]+' '+'|'+' '+indexList[3]+' ')
    print('-----------')
    print(' '+indexList[4]+' '+'|'+' '+indexList[5]+' '+'|'+' '+indexList[6]+' ')
    print('-----------')
    print(' '+indexList[7]+' '+'|'+' '+indexList[8]+' '+'|'+' '+indexList[9]+' ')
def playerInput():
    global currentPlayer
    currentChoice =input(f'Player {currentPlayer}, choose where to place {playerSign[currentPlayer]} (1-9): ')
    while currentChoice not in ['1','2','3','4','5','6','7','8','9'] or indexList[int(currentChoice)] != ' ':
        currentChoice =input(f'Chosen number coincides with a non-available slot. Choose again: ')
    currentChoice = int(currentChoice)
    indexList[currentChoice] = playerSign[currentPlayer]
    if currentPlayer == 1:
        currentPlayer = 2
    else:
        currentPlayer = 1
def checkWin():
    global win
    global winner
    global gamerunning
    if (indexList[1] == indexList[2] == indexList[3] and indexList[1] != ' '):
        win = True
        winner = indexList[1]
    elif (indexList[1] == indexList[4] == indexList[7] and indexList[1] != ' '):
        win = True
        winner = indexList[1]
    elif (indexList[1] == indexList[5] == indexList[9] and indexList[1] != ' '):
        win = True
        winner = indexList[1]
    elif (indexList[2] == indexList[5] == indexList[8] and indexList[2] != ' '):
        win = True
        winner = indexList[2]
    elif (indexList[3] == indexList[6] == indexList[9] and indexList[3] != ' '):
        win = True
        winner = indexList[3]
    elif (indexList[3] == indexList[5] == indexList[7] and indexList[3] != ' '):
        win = True
        winner = indexList[3]
    elif (indexList[4] == indexList[5] == indexList[6] and indexList[4] != ' '):
        win = True
        winner = indexList[4]
    elif (indexList[7] == indexList[8] == indexList[9] and indexList[7] != ' '):
        win = True
        winner = indexList[7]


    if win == True:
        if currentPlayer == 1:
            print(f'Player 2 has won!')
        else:
            print(f'Player 1 has won!')
        gamerunning = False
def checkDraw():
    global draw
    global gamerunning
    gamerunning = False
    draw = True
    for item in indexList.values():
        if item == ' ':
            draw = False
            gamerunning = True
            break

    if draw == True:
        print('Game ended in a draw!')
        gamerunning = False

print('Welcome to Tic Tac Toe! ')
replay = True
while replay:
    indexList = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    playerSign = {1:' ',2:' '}
    replay = False
    win = False
    draw = True
    gamerunning = True
    winner=''
    currentPlayer = 1
    replay = False
    initialPlayerChoose()

    while gamerunning:
        printBoard()
        checkDraw()
        checkWin()


        if draw or win:
            replayinput = input('Would you like to play again? (y/n)?: ')
            while replayinput not in ['y','n']:
                replayinput = input('Would you like to play again? (y/n)?:')

            if replayinput == 'y':
                replay = True
                break
            elif replayinput == 'n':
                replay = False
        else:
            playerInput()
