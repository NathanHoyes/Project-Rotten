from DatabaseConnector.DatabaseConnector import DatabaseConnector
from datetime import datetime


class WastageDatabaseConnector:

    select_by_id_sql = "SELECT * FROM wastage WHERE WasteID = %s"
    select_all_sql = "SELECT * FROM wastage"
    insert_sql = "INSERT INTO wastage (ProductID, Quantity, StaffID, LocationID, DateTimeRecorded) " \
                 "VALUES(%s, %s, %s, %s, %s)"
    database_connector = DatabaseConnector()

    def get_row_by_id(self, id: int) -> iter:
        params = (id, )
        return self.database_connector.executeSelectStatement(self.select_by_id_sql, params)

    def get_all_rows(self) -> iter:
        return self.database_connector.executeSelectStatement(self.select_all_sql, None)

    def insert_row(self, productID : int, quantity : int, staffID : int, locationID : int) -> None:
        if self.validate_insert(quantity):
            datetime_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            params = (productID, quantity, staffID, locationID, datetime_string)
            self.database_connector.executeUpdateStatement(self.insert_sql, params)

    def validate_insert(self, quantity : int) -> bool:
        return quantity > 0


    #TODO add additional search functionality - this will be very important
