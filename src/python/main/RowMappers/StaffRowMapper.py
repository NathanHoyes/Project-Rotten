from CredentialsManagement.Staff import Staff


class StaffRowMapper:

    # creates an admin object with the row results
    def map_row(self, row: list) -> Staff:
        return Staff(row[0], row[1], row[2], row[3], row[4])

    # creates a list of admin objects from the supplied query result
    def map_multiple_rows(self, query_result: iter) -> list:
        staff_result = []
        for staff in query_result:
            staff_result.append(self.map_row(staff))

        return staff_result
