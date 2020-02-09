import random

# Displaying Board
def display_board(board):
    print('\n' *50)
    print("\t\t\t============")
    print("\t\t\t GAME BOARD")
    print("\t\t\t============\n\n\n")
    print(f"\t\t\t {board[1]} | {board[2]} | {board[3]} ")
    print("\t\t\t---+---+---")
    print(f"\t\t\t {board[4]} | {board[5]} | {board[6]} ")
    print("\t\t\t---+---+---")
    print(f"\t\t\t {board[7]} | {board[8]} | {board[9]} ")


# Win_Check
def win_check(board, marker):
    return (
    # ROWS
    board[1] == board[2] == board[3] == marker or
    board[4] == board[5] == board[6] == marker or
    board[7] == board[8] == board[9] == marker or
    # COLS
    board[1] == board[4] == board[7] == marker or
    board[2] == board[5] == board[8] == marker or
    board[3] == board[6] == board[9] == marker or
    # DIAGONALS
    board[1] == board[5] == board[9] == marker or
    board[3] == board[5] == board[7] == marker
    )


# Replay Game
def replay():
    return input("\n\n\nEnter 'y' to Play Again! : ").lower().startswith('y')


# Randomly Choosing Player1 or Player 2
def player_select():
    return random.randint(1,2)
        

# Choosing Marker
def select_marker():
    marker = None
    while not (marker=='X' or marker=='O'):
        marker = input("\nDo you want 'X' or 'O' ? ").upper()
        if marker == 'X' or marker == 'O':
            break
        else:
            print("\nINVALID RESPONSE!\n")
    if marker == 'X':
        return ('X', 'O')
    elif marker == 'O':
        return('O', 'X')


# Space Check
def space_check(board,position):
    return board[position] == ' ' or board[position] == ''


# Board Full Check
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# Player Marker Placing
def player_move(board,position,marker):
    while not position in [1,2,3,4,5,6,7,8,9] or not space_check(board, position): 
        try :
            position = int(input("\nEnter in range (1,9): "))
            if position in [1,2,3,4,5,6,7,8]:
                if space_check(board, position):
                    pass
                else:
                    print("\n\nWRONG INPUT! Choose an empty space.")
            else:
                print("\n\nWRONG INPUT! Enter an input in range(1-9).")
            
        except:
            print("\n\nWRONG INPUT! Enter an input from the following : ")
            print("\n\t\t 1 | 2 | 3 ")
            print("\t\t---+---+---")
            print("\t\t 4 | 5 | 6 ")
            print("\t\t---+---+---")
            print("\t\t 7 | 8 | 9 ")
    board[position] = marker


# Duplicate Game Board
def copy_board(board):
    duplicate_board = []
    for i in board:
        duplicate_board.append(i)
    return duplicate_board


# Selecting a random move from the list
def select_random_move(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if space_check(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


# Placing Marker for CPU
def place_marker(board,position,marker):
    board[position] = marker


# CPU Move
def cpu_move(board, marker, difficulty):
    if difficulty == 1:
        position = None
        while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
            position = random.randint(1,9)
        return position
        
    elif difficulty == 2:
        if marker == 'X':
            comp_marker = 'X'
            player_marker = 'O'
        elif marker == 'O':
            comp_marker = 'O'
            player_marker = 'X' 
    
    # Win Check for CPU
        for i in range(1,10):
            copy = copy_board(board)
            if space_check(copy, i):
                copy[i] = comp_marker
                if win_check(copy, comp_marker):
                    return i
    # Block Player's Winning Move
        for i in range(1,10):
            copy = copy_board(board)
            if space_check(copy, i):
                copy[i] = player_marker
                if win_check(copy, player_marker):
                    return i
        
    # Corners if available
        move = select_random_move(board, [1, 3, 7, 9])
        if move != None:
            return move
    
    # Center if available
        if space_check(board, 5):
            return 5
    # Sides
        return select_random_move(board, [2, 4, 6, 8])





"""
                        ## CODING GAME NOW ##
"""

while True:    
    game_mode = None
    while not game_mode in range(1,4):
        print('\n' *100)
        print("\t\t\t++++++++++++++++++++++")
        print("\t\t\t......................")
        print("\t\t\tWELCOME TO TIC-TAC-TOE")
        print("\t\t\t......................")
        print("\t\t\t++++++++++++++++++++++")
        print("\n\n\n\n\t----------")
        print("\tGAME MODES ")
        print("\t----------")
        print("\n\n1 : \tSinglePlayer Mode")
        print("2 : \tMultiPlayer Mode")
        print("3 : \tExit Game")
        try:
            game_mode = int(input("\n\n\nSelect a mode to play : "))
            if game_mode == 1:
                print('\n' *50)
                print("\n\t\t--------------------------")
                print("\t\tSINGLE-PLAYER MODE(vs CPU)")
                print("\t\t--------------------------")
                
                print("\n\n\n\n\n\t________________")
                print("\n\tDIFFICULTY MODES ")
                print("\t________________")
                print("\n\n1 : \tEasy Mode")
                print("2 : \tHard Mode")
                print("3 : \tBack") 
                difficulty = None
                while not difficulty in range(1,4):
                    try:
                        difficulty = int(input("\nSelect a difficulty : "))
                        if difficulty <3:
                            pass
                        elif difficulty == 3:
                            game_mode = None
                        else:
                            print("\n\t________________")
                            print("\n\tDIFFICULTY MODES ")
                            print("\t________________")
                            print("\n1 : \tEasy Mode")
                            print("2 : \tHard Mode")
                            print("3 : \tBack") 
                            print("\nPlease enter a difficulty from the list")
                    except:
                        print("Please enter a valid input")
                
            elif game_mode == 2:
                print('\n' *50)
                print("\n\t\t----------------------------")
                print("\t\tMULTI-PLAYER MODE(vs PLAYER)")
                print("\t\t----------------------------")
            elif game_mode == 3:
                #print("\n\n\n\t\t----------------")
                print("\n\n\n\t\t_______________")
                print("\n\t\t...............")
                print("\t\t  GAME EXITED")
                print("\t\t...............")
                print("\t\t_______________")
                #print("\t\t----------------")
                print("\n")
            else:
                print("PLEASE ENTER A VALID OPTION")
        except:
            print("PLEASE ENTER A VALID OPTION")
    
    gameboard = [' '] * 10  # Empty board at first
    
    """
    SINGLEPLAYER
    """
    if game_mode == 1 and difficulty != 3:
        print("\n\nSelecting whether Player or CPU will play first randomly....\n")
        turn = player_select()
        if turn ==1:
            print("\nPlayer will play first..")
        else:
            print("\nCPU will play first..")
        
        print("\n\nPlayer ", end=' ')
        (player1_marker, cpu_marker) = select_marker()
        
        game_state = True
        
        
        while game_state:
            
            if turn == 1:
                display_board(gameboard)
                position = None
                print("\n\n")
                print("Player's turn")
                player_move(gameboard, position,player1_marker)
                # Checking win and draw
                if win_check(gameboard, player1_marker):
                    display_board(gameboard)
                    print("\n\n\n\t\t\t__________")
                    print("\n\t\t\tPlayer WON")
                    print("\t\t\t__________\n\n\n")
                    
                    game_state = False
                else:
                    if full_board_check(gameboard):
                        display_board(gameboard)
                        print("\n\n\n\t\t\t____")
                        print("\n\t\t\tDRAW")
                        print("\t\t\t____\n\n\n")         
                        game_state = False
                    else:
                        turn = 'CPU'
                
            else:
                display_board(gameboard)
                print("\n\n")
                print("CPU's turn")
                move = cpu_move(gameboard, cpu_marker, difficulty)
                place_marker(gameboard, move, cpu_marker)
                # Checking win and draw
                if win_check(gameboard, cpu_marker):
                    display_board(gameboard)
                    print("\n\n\n\t\t\t_______")
                    print("\n\t\t\tCPU WON")
                    print("\t\t\t_______\n\n\n")
                    game_state = False
                else:
                    if full_board_check(gameboard):
                        display_board(gameboard)
                        print("\n\n\n\t\t\t____")
                        print("\n\t\t\tDRAW")
                        print("\t\t\t____\n\n\n") 
                        game_state = False
                    else:
                        turn = 1
    
    """
    MULTIPLAYER
    """
    if game_mode == 2:
        print("\n\nSelecting A Player Randomly....\n")
        turn = player_select()
        #print(turn, " has been chosen\n")
        
        if turn == 1:
            print("\nPlayer1 has been chosen")
            (player1_marker, player2_marker) = select_marker()
        elif turn == 2:
            print("\nPlayer2 has been chosen")
            (player2_marker, player1_marker) = select_marker()
        
        game_state = True
                
        while game_state:
            
            if turn == 1:
                display_board(gameboard)
                position = None
                print("\n\n")
                print("Player1's turn")
                player_move(gameboard, position,player1_marker)
                # Checking win and draw
                if win_check(gameboard, player1_marker):
                    display_board(gameboard)
                    print("\n\n\n\t\t\t___________")
                    print("\n\t\t\tPlayer1 WON")
                    print("\t\t\t___________\n")
                    game_state = False
                else:
                    if full_board_check(gameboard):
                        display_board(gameboard)
                        print("\n\n\n\t\t\t____")
                        print("\n\t\t\tDRAW")
                        print("\t\t\t____\n\n\n") 
                        game_state = False
                    else:
                        turn = 2
                
            else:
                display_board(gameboard)
                position = None
                print("\n\n")
                print("Player2's turn")
                player_move(gameboard, position,player2_marker)
                # Checking win and draw
                if win_check(gameboard, player2_marker):
                    display_board(gameboard)
                    print("\n\n\n\t\t\t___________")
                    print("\n\t\t\tPlayer2 WON")
                    print("\t\t\t___________\n")
                    game_state = False
                else:
                    if full_board_check(gameboard):
                        display_board(gameboard)
                        print("\n\n\n\t\t\t____")
                        print("\n\t\t\tDRAW")
                        print("\t\t\t____\n\n\n") 
                        game_state = False
                    else:
                        turn = 1
                        
    if game_mode == 3 or not replay():
        break