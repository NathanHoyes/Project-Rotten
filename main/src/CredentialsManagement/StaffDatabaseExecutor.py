from DatabaseConnector.DatabaseConnector import DatabaseConnector


class StaffDatabaseExecutor:

    select_by_id_sql = "SELECT * FROM Staff WHERE StaffID = "
    select_all_sql = "SELECT * FROM Login"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id : int) -> iter:
        sql = self.select_by_id_sql + str(id)
        return self.database_connector.executeSelectStatement(sql)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql)