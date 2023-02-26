from unittest import TestCase
from ...main.RowMappers.StaffRowMapper import *
from ...main.DatabaseConnector.StaffDatabaseExecutor import StaffDatabaseExecutor
from ...main.DatabaseConnector.DatabaseConnector import DatabaseConnector

class Test(TestCase):

    executor = StaffDatabaseExecutor()
    db = DatabaseConnector()

    def test_map_row(self):
        self.setup_db()
        result = self.executor.get_row_by_id(1)
        staff = map_row(result)
        self.assertEqual(staff.staffID, 1)
        self.assertEqual(staff.loginID, 1)
        self.assertEqual(staff.firstName, "Andrew")
        self.assertEqual(staff.lastName, "Stevens")
        self.assertEqual(staff.locationID, 1)

    def test_map_multiple_rows(self):
        self.setup_db()
        result = self.executor.get_all_rows()
        staff_list = map_multiple_rows(result)
        staff = staff_list[1]
        self.assertEqual(staff.staffID, 2)
        self.assertEqual(staff.loginID, 1)
        self.assertEqual(staff.firstName, "Nathan")
        self.assertEqual(staff.lastName, "Hoyes")
        self.assertEqual(staff.locationID, 2)


    def setup_db(self):
        self.db.executeSqlScript("../../../resources/create_db_sql.sql")