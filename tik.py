from random import randrange

def DisplayBoard(board):
    for i in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   " + str(board[i][0]) + "   |   " + str(board[i][1]) + "   |   " + str(board[i][2]) + "   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")
        
def EnterMove(board):
    noEncontrado = 0
    correcto = True
    entrada = int(input("Ingresa tu movimiento: "))
    
    while correcto:
        if entrada < 1 or entrada > 9:
            print("Ingresa un numero entre 1 y 9")
            entrada = int(input("Ingresa tu movimiento: "))
        else:
            for board_row in board:
                if entrada in board_row:
                    index_of_value = board_row.index(entrada)
                    board_row[index_of_value] = "O"
                    correcto = False
                    break
                else:
                    noEncontrado += 1
                    
            if noEncontrado == 3:
                noEncontrado = 0
                print("Lugar Ocupado")
                entrada = int(input("Ingresa tu movimiento: "))

def MakeListOfFreeFields(board):
    free_fields = []
    for board_row in board:
        for field in board_row:
            if field != "O" and field != "X":
                free_fields.append((board.index(board_row), board_row.index(field)))
    if free_fields:
        return False
    else:
        return True

def VictoryFor(board, sign):
    for board_row in board:
        if board_row.count(sign) == 3:
            return True
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True

    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True

    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False

def DrawMove(board):
    correcto = True
    
    while correcto:
        entrada = randrange(1, 10)
        for board_row in board:
            if entrada in board_row:
                index_of_value = board_row.index(entrada)
                board_row[index_of_value] = "X"
                correcto = False
                break

def Main():
    board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
    DisplayBoard(board)

    while True:
        EnterMove(board)
        DisplayBoard(board)
        if (VictoryFor(board, "O")):
            print("¡¡¡Has ganado!!!")
            break
        if (MakeListOfFreeFields(board)):
            print("¡¡¡Empate!!!")
            break
        DrawMove(board)
        DisplayBoard(board)
        if (VictoryFor(board, "X")):
            print("¡¡¡Has perdido!!!")
            break
        if (MakeListOfFreeFields(board)):
            print("¡¡¡Empate!!!")
            break
    
Main()