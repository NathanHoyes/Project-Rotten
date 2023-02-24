from CredentialsManagement.Staff import Staff


# creates an admin object with the row results
def map_row(row: list) -> Staff:
    return Staff(row[0], row[1], row[2], row[3], row[4])


# creates a list of admin objects from the supplied query result
def map_multiple_rows(self, query_result: iter) -> list:
    staff_result = []

    row = next(query_result)

    while True:
        try:
            staff_result.append(Staff(row[0], row[1], row[2], row[3], row[4]))
            row = next(query_result)
        except StopIteration:
            break

    return staff_result
