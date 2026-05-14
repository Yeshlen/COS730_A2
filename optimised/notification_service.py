class NotificationService:
    def __init__(self):
        self.evaluationResult = ""

    def notifyResearcher(self, evaluationResult):
        print("NotificationService: notifyResearcher(evaluationResult) -", evaluationResult)
        self.evaluationResult = evaluationResult
        self.sendNotification()

    def sendNotification(self):
        print("NotificationService: sendNotification() -> Researcher:", self.evaluationResult)
        return self.evaluationResult
