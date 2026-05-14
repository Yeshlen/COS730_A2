from reviewer import Reviewer

class ReviewerManager:
    def __init__(self, databaseController):
        self.databaseController = databaseController

    def getAvailableReviewers(self):
        print("ReviewerManager: getAvailableReviewers()")
        reviewerList = self.databaseController.getReviewers()
        filteredReviewers = self.filterEligibleReviewers(reviewerList)
        return filteredReviewers

    def filterEligibleReviewers(self, reviewerList):
        print("ReviewerManager: filterEligibleReviewers(reviewerList) -", reviewerList)
        filteredReviewers = []

        for reviewer in reviewerList:
            if not reviewer["has_conflict"] and reviewer["workload"] <= 3:
                filteredReviewers.append(reviewer)

        return filteredReviewers

    def assignReviewers(self, filteredReviewers, data):
        print("ReviewerManager: assignReviewers(filteredReviewers, data) -", filteredReviewers, "-", data)
        reviewers = []

        for reviewerData in filteredReviewers:
            reviewer = Reviewer(reviewerData["name"])
            reviewer.assignReview(data)
            reviewers.append(reviewer)

        return reviewers
