from submission_controller import SubmissionController

class UI:
    def __init__(self):
        pass

    def submitResearchOutput(self, data):
        print("UI: submitResearchOutput(", data, ")")

        controller = SubmissionController()
        response = controller.submit(data)

        if response == "Invalid":
            print("Submission unsuccessful - Invalid format")
        else:
            print("Submission successful")
