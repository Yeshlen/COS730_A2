from evaluation_manager import EvaluationManager

class Reviewer:
    def __init__(self, name, evaluationManager):
        self.name = name
        self.evaluationManager = evaluationManager

    def assignReview(self, reviewer):
        print("Reviewer:", self.name, "assignReview(", reviewer, ")")

    def submitScore(self, score):
        print("Reviewer:", self.name, "submitScore(", score, ")")
        self.evaluationManager.submitScore(score)
