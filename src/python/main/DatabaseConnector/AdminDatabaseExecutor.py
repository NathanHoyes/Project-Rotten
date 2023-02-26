from src.python.main.DatabaseConnector.DatabaseConnector import DatabaseConnector


class AdminDatabaseExecutor:

    select_by_id_sql = "SELECT * FROM Admin WHERE AdminID = "
    select_all_sql = "SELECT * FROM Admin"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id : int) -> iter:
        sql = self.select_by_id_sql + str(id)
        return self.database_connector.executeSelectStatement(sql)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql)

    def insert_row(self, staffID : int) -> None:
        insert_sql = f"INSERT INTO admin (StaffID) VALUES({staffID})"
        self.database_connector.executeUpdateStatement(insert_sql)

    def delete_row(self, adminID : int) -> None:
        delete_sql = f"DELETE FROM admin WHERE AdminID = {adminID}"
        self.database_connector.executeUpdateStatement(delete_sql)
