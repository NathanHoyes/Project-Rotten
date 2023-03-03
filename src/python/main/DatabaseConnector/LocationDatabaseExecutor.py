from DatabaseConnector.DatabaseConnector import DatabaseConnector


class LocationDatabaseConnector:

    select_by_id_sql = "SELECT * FROM Locations WHERE LocationID = "
    select_all_sql = "SELECT * FROM Locations"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id : int) -> iter:
        sql = self.select_by_id_sql + str(id)
        return self.database_connector.executeSelectStatement(sql)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql)

    def insert_row(self, locationName : str) -> None:
        insert_sql = f"INSERT INTO Locations (LocationName) VALUES({locationName})"
        self.database_connector.executeUpdateStatement(insert_sql)

    def delete_row(self, locationID : int) -> None:
        delete_sql = f"DELETE FROM Locations WHERE LocationID = {locationID}"
        self.database_connector.executeUpdateStatement(delete_sql)
