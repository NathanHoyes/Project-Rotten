from CredentialsManagement.Admin import Admin


# creates an admin object with the row results
def map_row( row: list) -> Admin:
    return Admin(row[0], row[1])

    # creates a list of admin objects from the supplied query result


def map_multiple_rows(self, query_result: iter) -> list[Admin]:
    admin_result = []

    row = next(query_result)

    while True:
        try:
            admin_result.append(Admin(row[0], row[1]))
            row = next(query_result)
        except StopIteration:
            break

    return admin_result
