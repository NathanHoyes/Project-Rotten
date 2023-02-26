from DatabaseConnector.DatabaseConnector import DatabaseConnector


class LoginDatabaseExecutor:

    select_by_id_sql = "SELECT * FROM Logins WHERE LoginID = "
    select_all_sql = "SELECT * FROM Logins"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id : int) -> iter:
        sql = self.select_by_id_sql + str(id)
        return self.database_connector.executeSelectStatement(sql)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql)

    def insert_row(self, login_token : str, email : str) -> None:
        insert_sql = "INSERT INTO logins (LoginTokenHash, HashedEmail) " \
                     f"VALUES({login_token}, {email})"
        self.database_connector.executeUpdateStatement(insert_sql)

    def delete_row(self, LoginID : int) -> None:
        delete_sql = f"DELETE FROM logins WHERE LoginID = {LoginID}"
        self.database_connector.executeUpdateStatement(delete_sql)

