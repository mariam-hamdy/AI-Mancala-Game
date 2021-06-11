class Mancala:
    def __init__(self, board):
        if board!=None:
            self.board = board[:]
        else:
            self.board=[0 for i in range(14)]
            for i in range(0,6,1):
                self.board[i] = 4
            for i in range(7, 13, 1):
                self.board[i] = 4
    def game(self,currentPocket):
        i=currentPocket
        repeatTurn=False
        temp = self.board[i]
        self.board[i]=0
        if i >6:
            stones = temp
            while(stones>0):
                i = i+1
                nextPocket=i%14
                if nextPocket == 6:
                    continue
                    #nextPocket = 7
                    #self.board[nextPocket] = self.board[nextPocket] + 1
                else:
                    self.board[nextPocket] = self.board[nextPocket] + 1
                stones = stones - 1
            # stealing mode
            if nextPocket > 6 and self.board[nextPocket]==1 and nextPocket!=13 and self.board[12-nextPocket]!=0 \
                    and stones==0:
                self.board[13]= self.board[13] + 1 + self.board[12-nextPocket]
                self.board[nextPocket]=0
                self.board[12-nextPocket]=0
            #end of stealing mode
            if nextPocket == 13 and stones==0:
                repeatTurn=True
        else:
            stones = temp
            while(stones>0):
                i=i+1
                nextPocket = i%14
                if nextPocket==13:
                    continue
                    #nextPocket=0
                    #self.board[nextPocket] = self.board[nextPocket] + 1
                else:
                    self.board[nextPocket] = self.board[nextPocket] + 1
                stones = stones - 1
           if nextPocket < 6 and self.board[nextPocket]==1 and nextPocket!=6 and self.board[12-nextPocket]!=0 \
                    and stones==0:
                    self.board[6] = self.board[6] + 1 + self.board[12 - nextPocket]
                    self.board[nextPocket] = 0
                    self.board[12 - nextPocket] = 0
                # end of stealing
           if nextPocket == 6 and stones == 0:
                    repeatTurn = True
        return repeatTurn

    def gameWithoutStealing(self, currentPocket):
        i=currentPocket
        repeatTurn=False
        temp = self.board[i]
        self.board[i]=0
        if i >6:
            stones = temp
            while(stones>0):
                i = i+1
                nextPocket=i%14
                if nextPocket == 6:
                    continue
                    #nextPocket = 7
                    #self.board[nextPocket] = self.board[nextPocket] + 1
                else:
                    self.board[nextPocket] = self.board[nextPocket] + 1
                stones = stones -1
            # stealing mode
            #end of stealing mode
            if nextPocket == 13 and stones==0:
                repeatTurn=True
        else:
            stones = temp
            while(stones>0):
                i=i+1
                nextPocket = i%14
                if nextPocket==13:
                    continue
                    #nextPocket=0
                    #self.board[nextPocket] = self.board[nextPocket] + 1
                else:
                    self.board[nextPocket] = self.board[nextPocket] + 1
                stones = stones - 1
            # stealing mode
            #end of stealing mode
            if nextPocket == 6 and stones==0:
                repeatTurn=True
        return repeatTurn

    def isGameEnd(self):
        playerSide=0
        botSide=0
        for j in range(6):
            playerSide = playerSide + self.board[j]
            botSide = botSide + self.board[j+7]
        if playerSide == 0:
            self.board[13]= self.board[13]+botSide
            for k in range(6):
                self.board[k] = 0
                self.board[k + 7] = 0
            return True
        if botSide==0:
            self.board[6]=self.board[6]+ playerSide
            for k in range(6):
                self.board[k] = 0
                self.board[k + 7] = 0
            return True
        return False
    def printBoard(self):
        i = 0
        for stone in self.board:
            self.board[i] = int(self.board[i])
            if int(self.board[i]) < 10:
                self.board[i] = " " + str(self.board[i])
            else:
                self.board[i] = str(self.board[i])
            i = i + 1
        print("       12   11   10   9    8    7")
        print("+....+....+....+....+....+....+....+....+")
        print("|    | " + str(self.board[12]) + " | " + str(self.board[11]) + " | " + str(self.board[10]) +
              " | " + str(self.board[9]) + " | " + str(self.board[8]) +
              " | " + str(self.board[7]) + " |    |")
        print("| " + str(self.board[13]) + " |....+....+....+....+....+....| " + str(self.board[6]) + " |")
        print("|    | " + str(self.board[0]) + " | " + str(self.board[1]) + " | " +
              str(self.board[2]) + " | " + str(self.board[3]) + " | " + str(self.board[4]) + " | " + str(self.board[5])
              + " |    |")
        print("+....+....+....+....+....+....+....+....+")
        print("       0    1    2    3    4     5")
        print(" ")
        i = 0
        for stone in self.board:
            self.board[i] = int(self.board[i])
            i = i + 1

    def winner(self):
        if self.board[6] > self.board[13]:
            print("YOU IS THE WINNER")
        elif self.board[6] < self.board[13]:
            print("THE AI BOT IS THE WINNER")
        else:
            print("THE GAME ENDED")

    def heuristic(self):
        if self.isGameEnd():
            if self.board[13] > self.board[6]:
                return 100
            elif self.board[13] == self.board[6]:
                return 0
            else:
                return -100
        else:
            return self.board[13]-self.board[6]
def minimax_alphabeta(parent,depth,alpha,beta,minimax):
    if depth == 0 or parent.isGameEnd():
        return parent.heuristic(),-1
    if minimax:
        value = -1000000
        move = -1
        for i in range(7,13,1):
            if parent.board[i]==0:
                continue
            child = Mancala(parent.board[:])
            maximum = child.game(i)
            newValue,_ = minimax_alphabeta(child,depth-1,alpha,beta,maximum)
            if value < newValue:
                move = i
                value = newValue
            alpha = max(alpha,value)
            if alpha >= beta:
                break
        return value,move
    else:
        value = 1000000
        move = -1
        for i in range(0,6,1):
            if parent.board[i]==0:
                continue
            child= Mancala(parent.board[:])
            minimum= child.game(i)
            newValue,_ = minimax_alphabeta(child,depth-1,alpha,beta, not minimum)
            if value > newValue:
                move = i
                value = newValue
            beta = min(beta,value)
            if alpha >= beta:
                break
        return value,move
def minimax_noStealing(parent,depth,alpha,beta,minimax):
    if depth == 0 or parent.isGameEnd():
        return parent.heuristic(),-1
    if minimax:
        value = -1000000
        move = -1
        for i in range(7,13,1):
            if parent.board[i]==0:
                continue
            child = Mancala(parent.board[:])
            maximum = child.gameWithoutStealing(i)
            newValue,_ = minimax_alphabeta(child,depth-1,alpha,beta,maximum)
            if value < newValue:
                move = i
                value = newValue
            alpha = max(alpha,value)
            if alpha >= beta:
                break
        return value,move
    else:
        value = 1000000
        move = -1
        for i in range(0,6,1):
            if parent.board[i]==0:
                continue
            child= Mancala(parent.board[:])
            minimum= child.gameWithoutStealing(i)
            newValue,_ = minimax_alphabeta(child,depth-1,alpha,beta, not minimum)
            if value > newValue:
                move = i
                value = newValue
            beta = min(beta,value)
            if alpha >= beta:
                break
        return value,move

mancala=Mancala(None)
print(" ")
print("Let's Play Mancala")
mancala.printBoard()
chosenN=90
playing= True
player = int(input("for human player play first ENTER 1, for AI BOT play first ENTER 2 "))
print(" ")
stealing = int(input("To Enter Stealing mode WRITE 1 and to Enter Without Stealing mode WRITE 2 "))
if player == 1:
    if stealing == 1:
        while playing:
            if mancala.isGameEnd():
                mancala.winner()
                mancala.printBoard()
                break
            while True:
                if mancala.isGameEnd():
                    #mancala.winner()
                    break
                print("YOUR TURN")
                chosenN= int(input("write the number of pocket to play or -1 to quit the game "))
                if chosenN == -1:
                    playing=False
                    break
                if chosenN > 5 or mancala.board[chosenN] == 0:
                    print("wrong number or empty pocket")
                    chosenN= int(input("write the number of pocket to play or -1 to quit the game "))
                    #break
                temp=mancala.game(chosenN)
                mancala.printBoard()
                if not temp:
                    break
            while True:
                if mancala.isGameEnd():
                    #mancala.winner()
                    break
                if chosenN == -1:
                    playing=False
                    break
                print("AI BOT TURN")
                _,move = minimax_alphabeta(mancala,10,-100000,100000,True)
                print("AI BOT move is ",move)
                temp = mancala.game(move)
                mancala.printBoard()
                if not temp:
                    break

    elif stealing == 2:
        while playing:
            if mancala.isGameEnd():
                mancala.winner()
                mancala.printBoard()
                break
            while True:
                if mancala.isGameEnd():
                    #mancala.winner()
                    break
                print("YOUR TURN")
                chosenN= int(input("write the number of pocket to play or -1 to quit the game "))
                if chosenN == -1:
                    playing=False
                    break
                if chosenN > 5 or mancala.board[chosenN] == 0:
                    print("wrong number or empty pocket")
                    chosenN= int(input("write the number of pocket to play or -1 to quit the game "))
                    #break
                temp=mancala.gameWithoutStealing(chosenN)
                mancala.printBoard()
                if not temp:
                    break
            while True:
                if mancala.isGameEnd():
                    #mancala.winner()
                    break
                if chosenN == -1:
                    playing=False
                    break
                print("AI BOT TURN")
                _, move = minimax_noStealing(mancala, 10, -100000, 100000, True)
                print("AI BOT move is ", move)
                temp = mancala.gameWithoutStealing(move)
                mancala.printBoard()
                if not temp:
                    break
    else:
        stealing = int(input("To Enter Stealing mode WRITE 1 and to Enter Without Stealing mode WRITE 2 "))
elif player == 2:
    if stealing == 1:
        while playing:
            if mancala.isGameEnd():
                mancala.winner()
                mancala.printBoard()
                break
            while True:
                if mancala.isGameEnd():
                    #mancala.winner()
                    break
                if chosenN == -1:
                    playing=False
                    break
                print("AI BOT TURN")
                _,move = minimax_alphabeta(mancala,10,-100000,100000,True)
                print("AI BOT move is ",move)
                temp = mancala.game(move)
                mancala.printBoard()
                if not temp:
                    break
            while True:
                if mancala.isGameEnd():
                    #mancala.winner()
                    break
                print("YOUR TURN")
                chosenN= int(input("write the number of pocket to play or -1 to quit the game "))
                if chosenN == -1:
                    playing=False
                    break
                if chosenN > 5 or mancala.board[chosenN] == 0:
                    print("wrong number or empty pocket")
                    chosenN= int(input("write the number of pocket to play or -1 to quit the game "))
                    #break
                temp=mancala.game(chosenN)
                mancala.printBoard()
                if not temp:
                    break

    elif stealing == 2:
        while playing:
            if mancala.isGameEnd():
                mancala.winner()
                mancala.printBoard()
                break
            while True:
                if mancala.isGameEnd():
                    #mancala.winner()
                    break
                if chosenN == -1:
                    playing=False
                    break
                print("AI BOT TURN")
                _,move = minimax_noStealing(mancala,10,-100000,100000,True)
                print("AI BOT move is ",move)
                temp = mancala.gameWithoutStealing(move)
                mancala.printBoard()
                if not temp:
                    break
            while True:
                if mancala.isGameEnd():
                    #mancala.winner()
                    break
                print("YOUR TURN")
                chosenN= int(input("write the number of pocket to play or -1 to quit the game "))
                if chosenN == -1:
                    playing=False
                    break
                if chosenN > 5 or mancala.board[chosenN] == 0:
                    print("wrong number or empty pocket")
                    chosenN= int(input("write the number of pocket to play or -1 to quit the game "))
                    #break
                temp=mancala.gameWithoutStealing(chosenN)
                mancala.printBoard()
                if not temp:
                    break
    else:
        stealing = int(input("To Enter Stealing mode WRITE 1 and to Enter Without Stealing mode WRITE 2 "))
else:
    player = int(input("for human player play first ENTER 1, for AI BOT play first ENTER 2 "))
