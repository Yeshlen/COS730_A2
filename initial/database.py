class Database:
    def __init__(self):
        self.reviewerList = [
            {"name": "Alice", "has_conflict": False, "workload": 2},
            {"name": "Bob", "has_conflict": True, "workload": 5},
            {"name": "Charles", "has_conflict": False, "workload": 0},
            {"name": "Dave", "has_conflict": False, "workload": 3},
        ]

    def saveSubmission(self, data):
        print("Database: saveSubmission -", data)
        return "Database: confirmation"

    def fetchReviewers(self):
        print("Database: fetchReviewers()")
        return self.reviewerList

    def saveScore(self, score):
        print("Database: saveScore -", score)
        return True
