from database import Database

class DatabaseController:
    def __init__(self):
        self.database = Database()

    def saveSubmission(self, data):
        print("DatabaseController: saveSubmission -", data)
        saveStatus = self.database.saveSubmission(data)
        return saveStatus

    def getReviewers(self):
        print("DatabaseController: getReviewers()")
        reviewerList = self.database.getReviewers()
        return reviewerList

    def saveScore(self, score):
        print("DatabaseController: saveScore -", score)
        return self.database.saveScore(score)
