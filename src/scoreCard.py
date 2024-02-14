class scoreCard:
    def __init__(self, stringScoreCard=""):
        self.scoreCard = stringScoreCard
        self.scoreFrame1 = 0
        self.typeScoreValue = {
        "singleValue" : "123456789",
        "singleFailValue" : "-",
        "spareValue" : "/",
        "strikeValue" : "X"
        }
        self.equivSimbolsScoreValue = {
            "X" : 10,
            "-" : 0
        }

    def divideFrameScore(self):
        scoreList = []
        modScoreCard = self.scoreCard[:]
        while len(scoreList) < 9:
            scoreFrame = ''
        
            for value in modScoreCard:
                if value in self.typeScoreValue["singleValue"]:
                    scoreFrame = scoreFrame + value
                    if len(scoreFrame) == 2:
                        modScoreCard = modScoreCard[len(scoreFrame) : ]
                        break
                    else:
                        continue
                
                elif value in self.typeScoreValue["singleFailValue"]:
                    scoreFrame = scoreFrame + value
                    if len(scoreFrame) == 2:
                        modScoreCard = modScoreCard[len(scoreFrame) : ]
                        break
                    else:
                        continue
                
                elif value in self.typeScoreValue["spareValue"]:
                    scoreFrame = scoreFrame + value
                    modScoreCard = modScoreCard[len(scoreFrame) : ]
                    break

                elif value in self.typeScoreValue["strikeValue"]:
                    scoreFrame = scoreFrame + value
                    modScoreCard = modScoreCard[len(scoreFrame) : ]
                    break
                #Is missing an else, for cases where none of the specified value types are present.
            scoreList.append(scoreFrame)
        scoreList.append(modScoreCard)
        return scoreList




    def calcSimpleShot(self, scoreToSum):
        scoreToSum = [self.equivSimbolsScoreValue.get(element, element) for element in scoreToSum]
        scoreShotFrame = (int(shot) for shot in scoreToSum)
        scoreShotFrame = sum(scoreShotFrame)
        return scoreShotFrame

    #def calcSpareShot()
    #def calcStrikeShot()

    def calcStrikeShot(self, scoresToSum, next1_scoreShot="", next2_scoreShot=""):
        nexts_scoreShot = next1_scoreShot + next2_scoreShot
        strike_scoreToSum = []
        k = 0

        for value in nexts_scoreShot:
            k += 1
            if k == 3:
                break
            else:
                pass

            if value == 'X':
                strike_scoreToSum.append(self.equivSimbolsScoreValue['X'])
            elif value == '-':
                strike_scoreToSum.append(self.equivSimbolsScoreValue['-'])
            elif value in str(list(range(1, 10))):
                strike_scoreToSum.append(int(value))
        scoresToSum.append(sum(strike_scoreToSum))
        return sum(scoresToSum)

    def finalScore(self):
        divideFrameScore = scoreCard(self.scoreCard).divideFrameScore()
        result_finalScore = []
        for scoreFrame in divideFrameScore:
            scoresToSum = []

            for scoreShot in scoreFrame:
                if scoreShot in self.typeScoreValue["singleValue"]:
                    scoresToSum.append(scoreShot)
                elif scoreShot in self.typeScoreValue["singleFailValue"]:
                    scoresToSum.append(0)
                elif scoreShot in self.typeScoreValue['spareValue']:
                    scoresToSum = ['10']

                    if scoreFrame.index(scoreShot) == 1 and len(scoreFrame) == 3:
                        scoresToSum = ['10']
                        scoresToSum.append(scoreFrame[-1][-1])
                        result_finalScore.append(scoreCard(self.scoreCard).calcSimpleShot(scoresToSum))
                        break
                    else:
                        scoresToSum.append(divideFrameScore[divideFrameScore.index(scoreFrame) + 1][0])
                        result_finalScore.append(scoreCard(self.scoreCard).calcSimpleShot(scoresToSum))
                
                elif scoreShot in self.typeScoreValue['strikeValue']:
                    scoresToSum = [10]
                    if divideFrameScore[divideFrameScore.index(scoreFrame)] != divideFrameScore[-1]:
                        scoreCard(self.scoreCard).calcStrikeShot(scoresToSum, divideFrameScore[divideFrameScore.index(scoreFrame) + 1], divideFrameScore[divideFrameScore.index(scoreFrame) + 2])
                    else:
                        scoreCard(self.scoreCard).calcStrikeShot(scoresToSum)

                try:
                    if scoreShot == scoreFrame[-1] and scoreShot != '/' and scoreFrame[-2] != '/':
                        result_finalScore.append(scoreCard(self.scoreCard).calcSimpleShot(scoresToSum))
                    else:
                        pass
                except IndexError:
                    if scoreShot == scoreFrame[-1] and scoreShot != '/':
                        result_finalScore.append(scoreCard(self.scoreCard).calcSimpleShot(scoresToSum))
                    else:
                        pass

        return sum(result_finalScore)
'''

12345123451234512345

XXXXXXXXXXXX

9-9-9-9-9-9-9-9-9-9-

5/5/5/5/5/5/5/5/5/5/5

'''