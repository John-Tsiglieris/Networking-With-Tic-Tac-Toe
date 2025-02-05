import socket
import pickle

#HOST = socket.gethostname()
HOST = '192.168.1.76'
PORT = 12345
HEADERSIZE = 11

board = [[".",".","."],[".",".","."],[".",".","."]]
board_data = None
turn = 1

for row in board:
    print(row)

# establish connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()

client,addr = server.accept()






# ===================================================================================================
def checkWin():
    print("Testing: ", board)
    for row in board:
        if row == ["X","X","X"]:
            print("Player 1 wins!")
            return True
        elif row == ["O","O","O"]:
            print("Player 2 wins!")
            return True

    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" or board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" or board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" or board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" or board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("Player 1 wins!")
        sendMessage("Player 1 wins!")
        return True
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" or board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" or board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O" or board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O" or board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("Player 2 wins!")
        sendMessage("Player 2 wins!")
        return True
    return False
# ===================================================================================================






# ===================================================================================================
def sendMessage(message):
    client.sendall(message.encode('utf-8'))
# ===================================================================================================







while (turn <= 9):
    if (turn % 2 == 1): #Is player 1's turn
        while(True):
            print("Player 1 pick a row: ")
            while(True):
                row = input()
                if row:
                    if int(row) > 0 and int(row) <= 3:
                        row = int(row)
                        break
                    else:
                        print("Pick a valid number!")
                else:
                    print("Pick a valid number!")
            while(True):
                print("Player 1 pick a column: ")
                column = input()
                if column:
                    if int(column) > 0 and int(column) <= 3:
                        column = int(column)
                        break
                    else:
                        print("Pick a valid number!")
                else:
                    print("Pick a valid number!")
                
            if board[row-1][column-1] == ".":
                board[row-1][column-1] = "X"

                board_data = pickle.dumps(board)
                client.sendall(board_data)
                break
            else:
                print("Pick an empty spot")
    else:
        while(True):
            sendMessage("Player 2 pick a row: ")
            print("Player 2's turn")
            row = int(client.recv(1).decode('utf-8'))
            sendMessage("Player 2 pick a column: ")
            column = int(client.recv(1).decode('utf-8'))
            if board[row-1][column-1] == ".":
                board[row-1][column-1] = "O"
                break
            else: 
                sendMessage("Pick an empty spot")
    if checkWin():
        client.close()
        server.close()
        break
    turn += 1
    for row in board:
        print(row)
