from validator import Validator
from database import Database
from reviewer_manager import ReviewerManager
from reviewer import Reviewer
from evaluation_manager import EvaluationManager

class SubmissionController:
    def __init__(self):
        
        self.validator = Validator()
        self.database = Database()
        self.reviewerManager = ReviewerManager()
        self.evaluationManager = EvaluationManager()
        
    def submit(self, data):
        print("SubmissionController: submit(", data, ")")
        response = self.validator.validateFormat(data)
        
        if response:
            confirmation = self.database.saveSubmission(data)
            print(confirmation)

            self.filteredReviewers = self.reviewerManager.getAvailableReviewers()

            reviewers = []
            for reviewerData in self.filteredReviewers:
                reviewer = Reviewer(reviewerData["name"], self.evaluationManager)
                reviewer.assignReview(reviewerData)
                reviewers.append(reviewer)

            self.evaluationManager.startEvaluation()

            sampleScores = [8, 7, 9]
            for index, reviewer in enumerate(reviewers):
                score = sampleScores[index % len(sampleScores)]
                reviewer.submitScore(score)

            return self.evaluationManager.finishEvaluation()

        else:
            return "Invalid"

if __name__ == "__main__":
    controller = SubmissionController()


    controller.submit("Valid")
