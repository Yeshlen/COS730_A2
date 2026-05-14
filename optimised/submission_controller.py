from validator import Validator
from database_controller import DatabaseController
from reviewer_manager import ReviewerManager
from evaluation_manager import EvaluationManager
from notification_service import NotificationService

class SubmissionController:
    def __init__(self):
        self.validator = Validator()
        self.databaseController = DatabaseController()
        self.reviewerManager = ReviewerManager(self.databaseController)
        self.evaluationManager = EvaluationManager(self.databaseController)
        self.notificationService = NotificationService()

    def submit(self, data):
        print("SubmissionController: submit -", data)

        formatStatus = self.validator.validateFormat(data)

        if not formatStatus:
            return "submissionFailed"

        saveStatus = self.databaseController.saveSubmission(data)

        if not saveStatus:
            return "submissionFailed"

        filteredReviewers = self.reviewerManager.getAvailableReviewers()

        if len(filteredReviewers) == 0:
            return "submissionFailed"

        reviewers = self.reviewerManager.assignReviewers(filteredReviewers, data)
        
        evaluationResult = self.evaluationManager.startEvaluation(reviewers)
        self.notificationService.notifyResearcher(evaluationResult)

        return evaluationResult
