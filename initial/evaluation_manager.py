from database import Database
from notification_service import NotificationService

class EvaluationManager:
    def __init__(self):
        self.database = Database()
        self.notificationService = NotificationService()
        
        self.scores = []
        self.average = 0
        self.consensus = ""
        self.result = ""



    def startEvaluation(self):
        print("EvaluationManager: startEvaluation()")
        self.scores = []
        self.average = 0
        self.consensus = ""
        self.result = ""

    def submitScore(self, score):
        self.scores.append(score)
        self.database.saveScore(score)

    def finishEvaluation(self):
        self.average = self.calculateAverage()
        self.consensus = self.checkConsensus()
        self.result = self.applyRules()

        if self.result == "Accepted":
            self.notificationService.notifyAcceptance()
        elif self.result == "Rejected":
            self.notificationService.notifyRejection()
        else:
            self.notificationService.notifyRevision()

        return self.result

    def calculateAverage(self):
        print("EvaluationManager: calculateAverage()")
        self.average = sum(self.scores) / len(self.scores)
        return self.average

    def checkConsensus(self):
        print("EvaluationManager: checkConsensus()")
        
        if not self.scores:
            return False

        return max(self.scores) - min(self.scores) <= 2

    def applyRules(self):
        print("EvaluationManager: applyRules()")
        
        if self.average >= 7 and self.consensus:
            return "Accepted"
        elif self.average < 4:
            return "Rejected"
        else:
            return "Revision"
