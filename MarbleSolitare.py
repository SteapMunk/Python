
board = [
         [True for i in range(5)],
         [True for j in range(6)],
         [True for k in range(7)],
         [True for l in range(7)],
         [True for m in range(7)],
         [True for n in range(6)],
         [True for p in range(5)]
        ]
# True means filled with a marble, false is empty
board[0][0] = None
board[0][1] = None
board[1][0] = None
board[5][0] = None
board[6][1] = None
board[6][0] = None



def boardPrint():
    print("    0     1     2     3     4     5     6")
    for i in range(len(board)):
        print(i, board[i])
    print("Score = {}".format(score))

score = 0
#36 is max score

def playMove(inputI, indexI, inputF, indexF):
    if board[inputI][indexI] is None or board[inputF][indexF] is None:
        print("Bad Input")
    else:
        if board[inputI][indexI] and not board[inputF][indexF]:
            board[inputI][indexI] = False
            board[inputF][indexF] = True
            if (inputI - inputF) == 0:
                changeDir = 1 if indexI < indexF else -1
                board[inputI][indexI + changeDir] = False
            else:
                changeDir = 1 if inputI < inputF else -1
                board[inputI + changeDir][indexI] = False
            global score
            score = score + 1
        else:
            print("Bad Input")

def won():
    



board[3][3] = False
while True:
    boardPrint()
    inputI = int(input("Initial Row:"))
    indexI = int(input("Initial Column:"))
    inputF = int(input("Final Row:"))
    indexF = int(input("Final Column:"))
    playMove(inputI, indexI, inputF, indexF)

