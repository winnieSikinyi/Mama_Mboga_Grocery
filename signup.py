class sign_up:
    def __init__(self,firstname,lastname,username,password,confirmpassword,email):
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password
        self.confirmpassword=confirmpassword
        self.email=email
    def created_successfully(self):
        return "You have succefully signed up"