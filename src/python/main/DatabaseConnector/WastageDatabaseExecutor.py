from DatabaseConnector.DatabaseConnector import DatabaseConnector
from datetime import datetime


class WastageDatabaseConnector:

    select_by_id_sql = "SELECT * FROM wastage WHERE WasteID = "
    select_all_sql = "SELECT * FROM wastage"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id: int) -> iter:
        sql = self.select_by_id_sql + str(id)
        return self.database_connector.executeSelectStatement(sql)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql)

    def insert_row(self, productID : int, quantity : int, staffID : int, locationID : int) -> None:
        datetime_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        insert_sql = f"INSERT INTO wastage (ProductID, Quantity, StaffID, LocationID, DateTimeRecorded) " \
                     f"VALUES({productID}, {quantity}, {staffID}, {locationID}, '{datetime_string}')"
        self.database_connector.executeUpdateStatement(insert_sql)


    #TODO add additional search functionality - this will be very important
