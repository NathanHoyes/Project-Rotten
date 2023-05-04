from DatabaseConnector.DatabaseConnector import DatabaseConnector


class LoginDatabaseExecutor:

    select_by_id_sql = "SELECT * FROM Logins WHERE LoginID = %s"
    select_all_sql = "SELECT * FROM Logins"
    insert_sql = "INSERT INTO logins (LoginTokenHash, HashedEmail) " \
                 "VALUES(%s, %s)"
    delete_sql = "DELETE FROM logins WHERE LoginID = %s"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id : int) -> iter:
        params = (id, )
        return self.database_connector.executeSelectStatement(self.select_by_id_sql, params)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql, None)

    def insert_row(self, login_token : str, email : str) -> None:
        params = (login_token, email)
        self.database_connector.executeUpdateStatement(self.insert_sql, params)

    def delete_row(self, loginID : int) -> None:
        params = (loginID, )
        self.database_connector.executeUpdateStatement(self.delete_sql, params)

