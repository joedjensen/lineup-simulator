class SimpleGameState:
    def __init__(self, lineup):
        self.outs = 0
        self.inning = 1
        self.score = 0
        self.lineup = lineup
        self.lineupIndex = 0
        self.runners = [0] * 3
        self.gameInProgress = True

    def getCurrentHitter(self):
        return self.lineup[self.lineupIndex]

    def updateState(self, event):
        self.lineupIndex = (self.lineupIndex + 1) % len(self.lineup)
        match event:
            case 1 | 2 | 3  :
                i = 2
                while i >= 0:
                    if self.runners[i] == 1:
                        newIndex = i + event
                        if newIndex > 2:
                            self.score += 1
                        else:
                            self.runners[newIndex] = 1
                        self.runners[i] = 0
                    i -= 1
                self.runners[event - 1] = 1
            case 4:
                self.score += sum(self.runners) + 1
                self.runners = [0,0,0]

            case 5:
                i = 0
                # find first empty base
                while i < 3 and self.runners[i] == 1 :
                    i += 1
                if i < 3:
                    self.runners[i] = 1
                else:
                    self.score += 1
            case _:
                self.outs += 1
                if self.outs > 2:
                    self.inning += 1
                    self.outs = 0
                    self.runners = [0,0,0]
        if self.inning > 9:
            self.gameInProgress = False


