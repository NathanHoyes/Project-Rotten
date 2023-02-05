import hashlib

class CredentialsHasher():

    def __init__(self):
        self.hasher = hashlib.sha256()


    def hashValue(self, value: str) -> str:

        if self.validate(value):
            self.hasher.update(bytes(value, "utf-8"))
            return self.hasher.hexdigest()


    def createHashedLoginToken(self, hashedEmail : str, hashedPassword) -> str:
      self.hasher.update(bytes(hashedEmail + hashedPassword, "utf-8"))
      return self.hasher.hexdigest()


    def validate(self, value) -> bool:
        return type(value) == str
