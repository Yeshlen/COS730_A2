class Evaluator:
    def __init__(self):
        self.scores = []
        self.average = 0
        self.evaluationResult = ""

    def evaluateSubmission(self, scores):
        print("Evaluator: evaluateSubmission()")

        self.scores = scores
        self.average = self.calculateAverage()
        self.evaluationResult = self.checkConsensus()
        
        return self.evaluationResult

    def calculateAverage(self):
        print("Evaluator: calculateAverage()")
        
        return sum(self.scores) / len(self.scores)

    def checkConsensus(self):
        print("Evaluator: checkConsensus()")

        if self.average > 7:
            return "Accepted"
        elif self.average < 5:
            return "Rejected"
        else:
            return "Revision Needed"
