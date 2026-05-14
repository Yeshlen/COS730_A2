class Reviewer:
    def __init__(self, name):
        self.name = name

    def assignReview(self, data):
        print("Reviewer:", self.name, "assignReview(", data, ")")

    def submitScore(self, score):
        print("Reviewer:", self.name, "submitScore(", score, ")")
        return score
