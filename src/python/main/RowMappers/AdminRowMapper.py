from CredentialsManagement.Admin import Admin


class AdminRowMapper:

    # creates an admin object with the row results
    def map_row(self, row: list) -> Admin:
        return Admin(row[0], row[1])

    # creates a list of admin objects from the supplied query result
    def map_multiple_rows(self, query_result: iter) -> list:
        admin_result = []
        for admin in query_result:
            admin_result.append(self.map_row(admin))

        return admin_result
