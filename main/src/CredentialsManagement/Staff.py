class Staff():

    def __init__(self, staffID : int, loginID : int, 
                firstName : str, lastName : str, locationID : int):
        
        self.staffID = staffID
        self.loginID = loginID
        self.firstName = firstName
        self.lastName = lastName
        self.locationID = locationID

# this class will be used to hold a row of data from the staff table