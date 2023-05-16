class Customerfeedback:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.feedback = None

    def give_feedback(self, text):
        self.feedback = text

