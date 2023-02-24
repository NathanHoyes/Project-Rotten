class Login():

    def __init__(self, loginID : int, 
                loginTokenHash : str, 
                hashedEmail : str):

        self.loginID = loginID
        self.loginTokenHash = loginTokenHash
        self.hashedEmail = hashedEmail

# This class will be used to hold a row of data from the login table