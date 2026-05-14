from submission_controller import SubmissionController

class UI:
    def __init__(self):
        pass

    def submitResearchOutput(self, data):
        print("UI: submitResearchOutput(", data, ")")

        controller = SubmissionController()
        response = controller.submit(data)

        if response == "submissionFailed":
            print("Submission unsuccessful")
        else:
            print("Submission successful:", response)
