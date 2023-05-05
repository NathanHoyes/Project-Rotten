from DatabaseConnector.DatabaseConnector import DatabaseConnector


class LocationDatabaseConnector:

    select_by_id_sql = "SELECT * FROM Locations WHERE LocationID = %s"
    select_all_sql = "SELECT * FROM Locations"
    insert_sql = "INSERT INTO Locations (LocationName) VALUES(%s)"
    delete_sql = "DELETE FROM Locations WHERE LocationID = %s"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id : int) -> iter:
        params = (id, )
        return self.database_connector.executeSelectStatement(self.select_by_id_sql, params)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql, None)

    def insert_row(self, locationName : str) -> None:
        params = (locationName, )
        self.database_connector.executeUpdateStatement(self.insert_sql, params)

    def delete_row(self, locationID : int) -> None:
        params = (locationID, )
        self.database_connector.executeUpdateStatement(self.delete_sql, params)
