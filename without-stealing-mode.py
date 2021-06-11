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
                    nextPocket = 7
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
                    nextPocket=0
                else:
                    self.board[nextPocket] = self.board[nextPocket] + 1
                stones = stones - 1
                #stealing mode
                #end od stealing
                if nextPocket==6 and stones == 0:
                    repeatTurn=True
        return repeatTurn
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
