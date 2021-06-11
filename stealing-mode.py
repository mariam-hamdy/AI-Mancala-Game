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
                    nextPocket = 7
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
                    nextPocket=0
                else:
                    self.board[nextPocket] = self.board[nextPocket] + 1
                stones = stones - 1
                #stealing mode
                if nextPocket<6 and self.board[nextPocket]==1 and nextPocket!=6 and self.board[12-nextPocket]!=0\
                        and stones == 0:
                    self.board[6] = self.board[6] + 1 + self.board[12 - nextPocket]
                    self.board[nextPocket] = 0
                    self.board[12 - nextPocket] = 0
                #end of stealing
                if nextPocket==6 and stones==0:
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