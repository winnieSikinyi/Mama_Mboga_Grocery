class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):

      def sign_in(self, username, password):
        if self.username == username and self.password == password:
            return "Successfully signed in."
        else:
            return "Invalid username or password."