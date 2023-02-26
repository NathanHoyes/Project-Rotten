from DatabaseConnector.DatabaseConnector import DatabaseConnector


class StaffDatabaseExecutor:

    select_by_id_sql = "SELECT * FROM Staff WHERE StaffID = "
    select_all_sql = "SELECT * FROM Staff"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id : int) -> iter:
        sql = self.select_by_id_sql + str(id)
        return self.database_connector.executeSelectStatement(sql)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql)

    def insert_row(self, loginID : int, first_name : str, last_name : str, locationID :int) -> None:
        insert_sql = "INSERT INTO Staff (LoginID, FirstName, LastName, LocationID) " \
                     f"VALUES({loginID}, {first_name}, {last_name}, {locationID})"
        self.database_connector.executeUpdateStatement(insert_sql)

    def delete_row(self, staffID : int) -> None:
        delete_sql = f"DELETE FROM staff WHERE AdminID = {staffID}"
        self.database_connector.executeUpdateStatement(delete_sql)
