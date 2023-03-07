from unittest import TestCase
from RowMappers.WastageRowMapper import *
from DatabaseConnector.WastageDatabaseExecutor import WastageDatabaseConnector
from DatabaseConnector.DatabaseConnector import DatabaseConnector

class Test(TestCase):

    executor = WastageDatabaseConnector()
    db = DatabaseConnector()
    def test_map_row(self):
        self.setup_db()
        result = self.executor.get_row_by_id(1)
        wastage = map_row(result)
        self.assertEqual(wastage.wasteID, 1)
        self.assertEqual(wastage.productID, 1)
        self.assertEqual(wastage.quantity, 2)
        self.assertEqual(wastage.staffID, 1)
        self.assertEqual(wastage.locationID, 1)
        self.assertEqual(str(wastage.datetime_recorded), "2023-01-30 20:00:00")


    def test_map_multiple_rows(self):
        self.setup_db()
        result = self.executor.get_all_rows()
        wastage_list = map_multiple_rows(result)
        wastage = wastage_list[1]
        self.assertEqual(wastage.wasteID, 2)
        self.assertEqual(wastage.productID, 2)
        self.assertEqual(wastage.quantity, 4)
        self.assertEqual(wastage.staffID, 1)
        self.assertEqual(wastage.locationID, 1)
        self.assertEqual(str(wastage.datetime_recorded), "2023-01-30 20:10:00")

    def test_should_insert_row(self):
        self.setup_db()
        self.executor.insert_row(1, 1, 1, 1)
        result = self.executor.get_all_rows()
        wastage_list = map_multiple_rows(result)
        wastage = wastage_list[-1]
        self.assertEqual(wastage.productID, 1)
        self.assertEqual(wastage.quantity, 1)
        self.assertEqual(wastage.staffID, 1)
        self.assertEqual(wastage.locationID, 1)

    def setup_db(self):
        self.db.executeSqlScript("../../../resources/create_db_sql.sql")
