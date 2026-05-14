from evaluator import Evaluator

class EvaluationManager:
    def __init__(self, databaseController):
        self.databaseController = databaseController
        self.evaluator = Evaluator()
        self.scores = []
        self.evaluationResult = ""

    def startEvaluation(self, reviewers):
        print("EvaluationManager: startEvaluation()")
        self.scores = []

        sampleScores = [8, 7, 9]
        for index, reviewer in enumerate(reviewers):
            score = sampleScores[index % len(sampleScores)]
            score = reviewer.submitScore(score)
            self.databaseController.saveScore(score)
            self.scores.append(score)

        self.evaluationResult = self.evaluator.evaluateSubmission(self.scores)
        return self.evaluationResult
