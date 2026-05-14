from ui import UI

if __name__ == "__main__":
    ui = UI()

    print("=== Run 1: Invalid Submission ===")
    ui.submitResearchOutput("Invalid")

    print("\n\n")

    print("=== Run 2: Valid Submission ===")
    ui.submitResearchOutput("Valid")
