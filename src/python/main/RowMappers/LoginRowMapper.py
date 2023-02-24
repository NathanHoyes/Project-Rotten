from CredentialsManagement.Login import Login


# creates an admin object with the row results
def map_row(row_iterator: list) -> Login:
    row = next(row_iterator)
    return Login(row[0], row[1], row[2])


# creates a list of admin objects from the supplied query result
def map_multiple_rows(query_result: iter) -> list:
    login_result = []

    row = next(query_result)

    while True:
        try:
            login_result.append(Login(row[0], row[1], row[2]))
            row = next(query_result)
        except StopIteration:
            break

    return login_result
