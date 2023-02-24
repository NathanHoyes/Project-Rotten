class Login:

    def __init__(self, loginID: int,
                 loginTokenHash: str,
                 hashedEmail: str):
        self.loginID = loginID
        self.loginTokenHash = loginTokenHash
        self.hashedEmail = hashedEmail
