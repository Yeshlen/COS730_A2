class Validator:
    def __init__(self):
        pass

    def validateFormat(self, data):
        print("Validator: validateFormat(", data, ")")

        if data == "Valid":
            return True
        else:
            return False
