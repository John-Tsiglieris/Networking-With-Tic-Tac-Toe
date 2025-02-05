import socket
import pickle

#HOST = socket.gethostname()
HOST = '192.168.1.76'
PORT = 12345
HEADERSIZE = 11
board = None

# establish connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

data_chunks = None





# recieve and print data
def recieveBoard():
    print("recieving board")
    data_chunks = []
    '''
    while(True):
        chunk = client.recv(100)
        if not chunk:
            print("broken")
            break
        data_chunks.append(chunk)
    '''
    message = client.recv(1000) # temp
    data_chunks.append(message)
    
    print("deserializing data")
    # deserialize data
    data = b"".join(data_chunks)
    board = pickle.loads(data)
    data_chunks = []
    return board




def receiveMessage():
    new_msg = True
    msg = client.recv(11)
    msg = None
    if new_msg:
        msglen = int(msglen[:HEADERSIZE])
        new_msg = False

    msg += 1





# GAME LOOP
while(True): # keep the loop going indefinitely until connection closed
    # Recieve and unpickle the board
    board = recieveBoard()
    for row in board:
        print(row)

    # Recieve and print message from server to input row
    print("Player 2 input row")
    #print(recieveMessage())
    client.recv(21).decode('utf-8')
    row = input()
    client.sendall(row.encode('utf-8'))
    
    # Recieve and print message from server to input column
    print("Player 2 input column")
    #print(recieveMessage())
    client.recv(24).decode('utf-8')
    column = input()
    client.sendall(column.encode('utf-8'))

    print("Row: ", row, " Row type: ", type(row))
    print("Column: ", column, " Column type: ", type(column))
    # Display the board
    if board[int(row)-1][int(column)-1] == ".":
        board[int(row)-1][int(column)-1] = "O"

    print(board)
    
    
