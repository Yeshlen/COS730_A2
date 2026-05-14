from database import Database

class ReviewerManager:
    def __init__(self):
        self.reviewerList = []
        self.db = Database()

    def getAvailableReviewers(self):
        print("ReviewerManager: getAvailableReviewers()")
        self.reviewerList = self.db.fetchReviewers()
        filteredReviewers = self.filterConflicts(self.reviewerList)
        filteredReviewers = self.checkWorkload(filteredReviewers)
        
        return filteredReviewers


    def filterConflicts(self, reviewerList):
        print("ReviewerManager: filterConflicts -", reviewerList)
        filteredReviewers = []
        
        for reviewer in reviewerList:
            if not reviewer["has_conflict"]:
                filteredReviewers.append(reviewer)

        return filteredReviewers

    def checkWorkload(self, reviewerList):
        print("ReviewerManager: checkWorkload -", reviewerList)
        filteredReviewers = []

        for reviewer in reviewerList:
            if reviewer["workload"] <= 3:
                filteredReviewers.append(reviewer)
        
        return filteredReviewers


if __name__ == "__main__":
    manager = ReviewerManager()
    print([reviewer["name"] for reviewer in manager.getAvailableReviewers()])   
