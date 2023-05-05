from DatabaseConnector.DatabaseConnector import DatabaseConnector


class StaffDatabaseExecutor:

    select_by_id_sql = "SELECT * FROM Staff WHERE StaffID = %s"
    select_all_sql = "SELECT * FROM Staff"
    insert_sql = "INSERT INTO Staff (LoginID, FirstName, LastName, LocationID) " \
                 "VALUES(%s, %s, %s, %s)"
    delete_sql = "DELETE FROM staff WHERE AdminID = %s"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id : int) -> iter:
        params = (id, )
        return self.database_connector.executeSelectStatement(self.select_by_id_sql, params)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql, None)

    def insert_row(self, loginID : int, first_name : str, last_name : str, locationID :int) -> None:
        params = (loginID, first_name, last_name, locationID)
        self.database_connector.executeUpdateStatement(self.insert_sql, params)

    def delete_row(self, staffID : int) -> None:
        params = (staffID, )
        self.database_connector.executeUpdateStatement(self.delete_sql, params)
