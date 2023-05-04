from DatabaseConnector.DatabaseConnector import DatabaseConnector


class AdminDatabaseExecutor:

    select_by_id_sql = "SELECT * FROM Admin WHERE AdminID = %s"
    select_all_sql = "SELECT * FROM Admin"
    delete_by_id_sql = "DELETE FROM admin WHERE AdminID = %s"
    insert_admin_sql = "INSERT INTO ADMIN (StaffID) VALUES (%s)"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id : int) -> iter:
        params = (id, )
        return self.database_connector.executeSelectStatement(self.select_by_id_sql, params)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql, None)

    def insert_row(self, staffID : int) -> None:
        params = (staffID,)
        self.database_connector.executeUpdateStatement(self.insert_admin_sql, params)

    def delete_row(self, adminID : int) -> None:
        params = (adminID, )
        self.database_connector.executeUpdateStatement(self.delete_by_id_sql, params)
