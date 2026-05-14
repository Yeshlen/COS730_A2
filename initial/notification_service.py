class NotificationService:
    def __init__(self):
        self.result = ""

    def notifyAcceptance(self):
        print("NotificationService: notifyAcceptance()")

        self.result = "Accepted"
        self.sendNotification()

    def notifyRejection(self):
        print("NotificationService: notifyRejection()")

        self.result = "Rejected"
        self.sendNotification()

    def notifyRevision(self):
        print("NotificationService: notifyRevision()")

        self.result = "Revision Requested"
        self.sendNotification()

    def sendNotification(self):
        print("NotificationService: sendNotification() -> Researcher:", self.result)
        return self.result
