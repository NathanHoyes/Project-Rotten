from CredentialsManagement.Login import Login


# creates an admin object with the row results
def map_row(self, row: list) -> Login:
    return Login(row[0], row[1], row[2])


# creates a list of admin objects from the supplied query result
def map_multiple_rows(self, query_result: iter) -> list[Login]:
    login_result = []
    for login in query_result:
        login_result.append(self.map_row(login))

    return login_result
